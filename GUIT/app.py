import os    
import re    
import io    
import csv   
import pandas as pd    
from datetime import datetime   
from flask import Flask, jsonify, render_template, request, Response, stream_with_context    
from PIL import Image, ImageDraw, ImageFont    
from config import (color_name_to_rgb, font_to_uni)
from deskplates_config import (    
    sku_to_image as deskplates_sku_to_image,    
    sku_to_font as deskplates_sku_to_font,    
    sku_to_fontsize_placement as deskplates_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as deskplates_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as deskplates_sku_to_second_line_font,    
    get_font_color_for_dswclr001,    
)    
from tumbler_config import (    
    sku_to_image as tumbler_sku_to_image,    
    sku_to_font as tumbler_sku_to_font,    
    sku_to_fontsize_placement as tumbler_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as tumbler_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as tumbler_sku_to_second_line_font,    
    skip_line as tumbler_skip_line,    
    process_font_color,  process_special_rules,  
)  
from neckless_config import (  
    sku_to_image as nck_sku_to_image,    
    sku_to_fontsize_placement as nck_sku_to_fontsize_placement,
    design_to_font, design_to_sku_to_second_fontsize_placement, design_to_sku_to_third_fontsize_placement, design_to_sku_to_fourth_fontsize_placement,
    
)  
from ring_config import (     
    sku_to_font as rng_sku_to_font,    
    sku_to_fontsize_placement as rng_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as rng_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as rng_sku_to_second_line_font,   
    rng_sku_needs_white_background, rng_sku_to_image_one_line, rng_sku_to_image_two_line, 
    handle_rng_skus, draw_white_background_if_needed,
)  
# Merge dictionaries    
sku_to_image = {**deskplates_sku_to_image, **tumbler_sku_to_image, **nck_sku_to_image}    
sku_to_font = {**deskplates_sku_to_font, **tumbler_sku_to_font, **rng_sku_to_font}    
sku_to_fontsize_placement = {**deskplates_sku_to_fontsize_placement, **tumbler_sku_to_fontsize_placement, **nck_sku_to_fontsize_placement, **rng_sku_to_fontsize_placement}    
sku_to_second_fontsize_placement = {**deskplates_sku_to_second_fontsize_placement, **tumbler_sku_to_second_fontsize_placement, **rng_sku_to_second_fontsize_placement}    
sku_to_second_line_font = {**deskplates_sku_to_second_line_font, **tumbler_sku_to_second_line_font, **rng_sku_to_second_line_font}    
skip_line = {**tumbler_skip_line}    
  
csv_load_count = 0   
  
def process_personalization_text(text, clean_sku):      
    lines = [line for line in text.split('\n') if line.strip()]      
    lines = [re.sub(r'(line \d+: ?|name[s]?: ?|title[s]?: ?|top name[s]?: ?|bottom name[s]?: ?|kids name[s]?: ?)', '', line, flags=re.IGNORECASE).strip('\r') for line in lines]      
    lines = [line for line in lines if line.strip()]      
      
    processed_lines = []      
    for line_index, line in enumerate(lines):      
        line = re.sub(r',$', '', line)  # Remove comma at the end of the line  
  
        for text, skus in skip_line["line1"].items():      
            if clean_sku in skus:      
                pattern = re.compile(text, flags=re.IGNORECASE)      
                line = pattern.sub('', line).strip()      
      
        for text, skus in skip_line["line2"].items():      
            if clean_sku in skus and line_index == 1:      
                pattern = re.compile(text, flags=re.IGNORECASE)      
                line = pattern.sub('', line).strip()      
      
        processed_line = process_special_rules(clean_sku, line, line_index)  
  
        # remove  
        processed_line = re.sub(r',\s*chain:\s*Box Chain', '', processed_line)   
        processed_line = re.sub(r',\s*font:\s*Claster Regular', '', processed_line)   
   
        # unicoded last letter    
        if clean_sku.startswith("NCK") or (clean_sku.startswith("RNG") and line_index == 1):    
            last_char = processed_line[-1].lower()    
            unicode_code = font_to_uni.get(last_char)    
            if unicode_code:    
                processed_line = processed_line[:-1] + chr(int(unicode_code, 16))    
            else:    
                print(f"Warning: Unicode character not found for '{last_char}'.")    
     
      
        processed_lines.append(processed_line)      
      
    return '\n'.join(processed_lines)   
    
# Load font from the given font path and font size    
def load_font(font_path, font_size):    
    try:    
        font = ImageFont.truetype(font_path, font_size)    
    except OSError:    
        print(f"Error loading font: {font_path}. Using default font.")    
        font = ImageFont.load_default()    
    return font    
    
def get_font_path(clean_sku):    
    font_path = sku_to_font.get(clean_sku, 'arial.ttf')    
    return font_path    

# line placement 
def calculate_font_size_and_placement(sku, text, num_chars, item_options):      
    max_x = sku_to_fontsize_placement.get(sku, {}).get("max_x", 3700)      
      
    if sku.startswith("NCK"):    
        design_font_match = re.search(r'Design:\s*([\w\s-]+)', item_options)    
        if design_font_match:    
            design_font = design_font_match.group(1)    
            if design_font in design_to_font:    
                values = sku_to_fontsize_placement.get(design_font, {}).get(num_chars, (200, None, 100))    
            else:    
                values = sku_to_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))    
        else:    
            values = sku_to_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))    
    elif sku.startswith("RNG"):    
        font_size, x, y = sku_to_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))    
        font = load_font(get_font_path(sku), font_size)    
        left, _, right, _ = font.getbbox(text)    
        text_width = right - left    
        x = max_x - text_width    
        return font_size, x, y    
    else:    
        values = sku_to_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))    
      
    if len(values) == 2:      
        font_size, y = values      
        x = None      
    else:      
        font_size, x, y = values      
    print(f"Num chars: {num_chars}")      
    return font_size, x, y  
# line 2    
def calculate_second_font_size_and_placement(sku, num_chars, item_options):      
    if sku.startswith("NCK"):  
        design_font_match = re.search(r'Design:\s*([\w\s-]+)', item_options)  
        if design_font_match:  
            design_font = design_font_match.group(1)  
            if design_font in design_to_sku_to_second_fontsize_placement:  
                font_size, x, y = design_to_sku_to_second_fontsize_placement[design_font]  
            else:   
                font_size, x, y = get_font_size_placement_from_sku(sku, num_chars)  
        else:  
            font_size, x, y = get_font_size_placement_from_sku(sku, num_chars)  
    else:  
        font_size, x, y = get_font_size_placement_from_sku(sku, num_chars)  
  
    return font_size, x, y
# line 3 
def calculate_third_font_size_and_placement(sku, num_chars, item_options):      
    if sku.startswith("NCK"):  
        design_font_match = re.search(r'Design:\s*([\w\s-]+)', item_options)  
        if design_font_match:  
            design_font = design_font_match.group(1)  
            if design_font in design_to_sku_to_third_fontsize_placement:  
                font_size, x, y = design_to_sku_to_third_fontsize_placement[design_font]  
            else:  
                font_size, x, y = 200, None, 100  
        else:   
            font_size, x, y = 200, None, 100  
    else:    
        font_size, x, y = 200, None, 100  

    return font_size, x, y 
# line 4
def calculate_fourth_font_size_and_placement(sku, num_chars, item_options):      
    if sku.startswith("NCK"):  
        design_font_match = re.search(r'Design:\s*([\w\s-]+)', item_options)  
        if design_font_match:  
            design_font = design_font_match.group(1)  
            if design_font in design_to_sku_to_fourth_fontsize_placement:  
                font_size, x, y = design_to_sku_to_fourth_fontsize_placement[design_font]  
            else:   
                font_size, x, y = 200, None, 100  
        else:  
            font_size, x, y = 200, None, 100  
    else:  
        font_size, x, y = 200, None, 100  
  
    return font_size, x, y

def get_font_size_placement_from_sku(sku, num_chars):  
    sku_fontsize_placement = sku_to_second_fontsize_placement.get(sku, {})      
    values = sku_fontsize_placement.get(num_chars, (200, None, 100))      
    if len(values) == 2:      
        font_size, y = values      
        x = None      
    else:      
        font_size, x, y = values  
      
    return font_size, x, y  
   

# error skus     
def create_check_csv_image():    
    image = Image.new('RGB', (3250, 1750), color='white')    
    draw = ImageDraw.Draw(image)    
    font = load_font('arial.ttf', 200)    
    text = "Reupload to PreCheck"    
    left, _, right, _ = font.getbbox(text)    
    text_width = right - left    
    text_x = (3250 - text_width) // 2    
    text_y = (1750 - 200) // 2    
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)    
    return image    
    
# white background for RNG   
def draw_white_background(draw, x, y, text_width, text_height, margin_left=0, margin_right=-60, margin_top=0, margin_bottom=0):  
    draw.rectangle([x + margin_left, y + margin_top, x + text_width + margin_right, y + text_height + margin_bottom], fill=(255, 255, 255))   
  
# Process each row from the dataframe    
def process_row(index, row, folder_name):      
    # extract clean SKU and background image path from the row      
    sku = row['Item - SKU']      
    order_number = str(row['Order - Number']).strip('"')    
    item_options = str(row['Item - Options'])     
    
    clean_sku_match = re.search(r"(?:DSWCLR001)?UVP[A-Z0-9]+", sku)      
    if not clean_sku_match:      
        clean_sku_match = re.search(r"RNG[A-Z0-9]+", sku)      
    if not clean_sku_match:        
        clean_sku_match = re.search(r"NCK[A-Z0-9]+", sku)       
    if not clean_sku_match:      
        return 
  
    if not clean_sku_match:    
        return    
    clean_sku = clean_sku_match.group(0)    
    background_image_path = sku_to_image.get(clean_sku)  
    
    font_path = get_font_path(clean_sku)    
    
    inscriptions_match = re.findall(r'(?:Left|Right) Inscription:\s*([\s\S]+?)(?:,|$)', str(item_options))  
    
    if inscriptions_match:  
        personalization_text = '\n'.join(inscriptions_match).strip()  
    else:  
        match = re.search(r'(?:Personalization|Custom Name):([\s\S]+)', str(item_options))  
        if match:  
            personalization_text = match.group(1)  
        else:  
            personalization_text = ''  
    
    
    lines = [line for line in personalization_text.split('\n') if line.strip()]    
    lines = [re.sub(r'Line \d+: ?', '', line).strip('\r') for line in lines]    
    lines = [line.strip() for line in lines if line.strip()]    

    # ERROR does not reconize sku or the lines in sku   
    if not lines:    
        image = create_check_csv_image()    
        image_name = f"{order_number}_{sku}_{index}.png"    
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), image_name)    
        image.save(image_path)    
        print(f"Error: list index out of range, saved {order_number}_{sku}_{index}.png")    
        return    
    else:    
        num_chars_line1 = len(lines[0])

    # handle RNG skus
    background_image_path = handle_rng_skus(clean_sku, lines, rng_sku_to_image_one_line, rng_sku_to_image_two_line, background_image_path)  
 
    # Add a check to skip the text specified in the skip_line dictionary    
    skip_text = skip_line.get("skip_line1_text", {}).get(clean_sku)    
    
    if len(lines) > 0:    
        print(f"First line before checking: {lines[0]}")    
    
    if skip_text and len(lines) > 0 and lines[0] == skip_text:    
        lines.pop(0)    
        print(f"First line removed: {lines}")

    # Apply special rules to split sku for different design options
    design_option_match = re.search(r'Design Options:\s*([\w\s-]+)', str(row['Item - Options']))  
    if design_option_match:  
        design_option = design_option_match.group(1).upper().replace(" ", "_")  
        if clean_sku == 'UVPPSBASTUVP':  
            background_image_path = sku_to_image.get(f'{clean_sku}-{design_option}') 

    # Apply special rules to personalization text and font color    
    processed_text = process_personalization_text(personalization_text, clean_sku)    
    lines = [line for line in processed_text.split('\n') if line.strip()]    
    
    num_chars_line1 = len(lines[0])    
    font_size_line1, x_line1, y_line1 = calculate_font_size_and_placement(clean_sku, lines[0], num_chars_line1, item_options)  
    
    if len(lines) > 1:    
        num_chars_line2 = len(lines[1])    
        font_size_line2, x_line2, y_line2 = calculate_second_font_size_and_placement(clean_sku, num_chars_line2, item_options)      
    else:    
        font_size_line2, x_line2, y_line2 = None, None, None 

    if len(lines) > 2:  
        num_chars_line3 = len(lines[2])  
        font_size_line3, x_line3, y_line3 = calculate_third_font_size_and_placement(clean_sku, num_chars_line3, item_options) 

    if len(lines) > 3:  
        num_chars_line4 = len(lines[3])  
        font_size_line4, x_line4, y_line4 = calculate_fourth_font_size_and_placement(clean_sku, num_chars_line4, item_options)  
            
    # Create image with personalized text    
    image = Image.open(background_image_path) if background_image_path else Image.new('RGB', (3250, 1750), color='white')    
    draw = ImageDraw.Draw(image)    
    image_width, _ = image.size    
    
    # hard set the font color
    if clean_sku.startswith(("RNG", "NCK")):  
        font_color = (0, 0, 0)    
    elif not clean_sku.startswith("DSWCLR001"):   
        design_color_match = re.search(    
            r'(?:Color of Text|Design Option & Color|Font Color|Design(?: Colors?)?|Custom Text Color):\s*([\w\s]+)',    
            item_options)    
        if design_color_match:    
            design_color_text = design_color_match.group(1).lower()    
        else:    
            design_color_text = "white"    
        font_color = color_name_to_rgb.get(design_color_text, (255, 255, 255))    
    else:    
        font_color = get_font_color_for_dswclr001(clean_sku)    
    
    processed_font_color = process_font_color(font_color, clean_sku)
  
    # Draw each line separately      
    for i, line in enumerate(lines):      
        # Load the font for the current line      
        font_path = sku_to_second_line_font.get(clean_sku, font_path) if i == 1 else get_font_path(clean_sku)     
    
        # Handle NCK SKUs    
        if clean_sku.startswith("NCK"):    
            design_font_match = re.search(r'Design:\s*([\w\s-]+)', item_options)    
            if design_font_match:    
                design_font = design_font_match.group(1)    
                if design_font in design_to_font:    
                    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', design_to_font[design_font])    
                else:    
                    print(f"Warning: Design '{design_font}' not found in design_to_font dictionary. Using default font.")    
                    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'arial.ttf')    
    
        font_size = font_size_line1  
        if i == 1: 
            font_size = font_size_line2  
        elif i == 2:
            font_size = font_size_line3  
        elif i == 3: 
            font_size = font_size_line4  
    
        font = load_font(font_path, font_size)      
    
        text_y = y_line1  
        if i == 1: 
            text_y = y_line2  
        elif i == 2: 
            text_y = y_line3  
        elif i == 3:  
            text_y = y_line4  
    
        # center the text if x-coordinate is not provided      
        if i == 1 and x_line2 is not None:      
            text_x = x_line2      
        elif x_line1 is not None:      
            text_x = x_line1      
        else:      
            left, _, right, _ = font.getbbox(line)      
            text_width = right - left      
            text_x = (image_width - text_width) // 2      
        
        # white background behind the text if the SKU starts with "RNG"      
        draw_white_background_if_needed(clean_sku, rng_sku_needs_white_background, font, line, text_x, text_y, draw_white_background, draw)    
            
        # Draw the current line      
        draw.text((text_x, text_y), line, fill=processed_font_color, font=font)      
     
  
    
    # name the saved png
    def generate_file_name(order_number, sku, index, tumbler_color_text=None):    
        if tumbler_color_text and tumbler_color_text != "unknown_color":    
            return f"{order_number}_{sku}_{tumbler_color_text}_{index}.png"    
        else:    
            return f"{order_number}_{sku}_{index}.png"    
    
    tumbler_color_match = re.search(    
        r'(?:Tumbler )?Color(?:s)?: ([^,]+)', str(item_options))    
    tumbler_color_text = tumbler_color_match.group(1).replace(" ", "_") if tumbler_color_match else "unknown_color"    
    
    # Save image
    image_name = generate_file_name(order_number, sku, index, tumbler_color_text)  
  
    # Create separate folders for JEWELRY SKUs  
    if clean_sku.startswith("RNG"):  
        sub_folder_name = 'RNG'  
    elif clean_sku.startswith("NCK02"):  
        sub_folder_name = 'NCK02'  
    elif clean_sku.startswith("NCK03"):  
        sub_folder_name = 'NCK03'  
    elif clean_sku.startswith("NCK04"):  
        sub_folder_name = 'NCK04'  
    else:  
        sub_folder_name = ''  
  
    if sub_folder_name:  
        sub_folder_path = os.path.join(folder_name, sub_folder_name)  
        if not os.path.exists(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path)):  
            os.makedirs(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path))  
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path, image_name)  
    else:  
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), folder_name, image_name)  
      
    image.save(image_path)     
    
    print(f"Final personalization text: {personalization_text}")    
    print(f"Final font color: {font_color}")    
    
# Export images from the given dataframe    
def export_images(df, full_folder_path):  
    if df.empty:    
        return {"error": "Please load a CSV file first."}    
    
    for index, row in df.iterrows():    
        if pd.isna(row['Item - SKU']):    
            continue    
        process_row(index, row, full_folder_path)    
    
    return {"message": f"Images exported to {full_folder_path}!"} 

# design window loading screen    
def processing_generator(csv_data, folder_name):  
     
    csv_reader = csv.DictReader(csv_data)    
    rows = [row for row in csv_reader]    
      
    df = pd.DataFrame(rows)    
    
    processed_count = 0
    
    for index, row in df.iterrows():    
        if pd.isna(row['Item - SKU']) or row['Item - SKU'] == "":    
            continue    
        process_row(index, row, folder_name)    
        processed_count += 1    
        progress_message = f"Processed order {row['Order - Number']}, {row['Item - SKU']}: {index}\n"     
        yield progress_message    
    
    yield f"Processing complete. Processed {processed_count} rows."   
  
# Flask app setup    
app = Flask(__name__)   
    
@app.route('/')    
def home():    
    return render_template('home.html')    
    
@app.route('/precheck')    
def precheck():    
    return render_template('precheck.html')    
    
@app.route('/designer')    
def designer():    
    return render_template('designer.html')    
    
@app.route('/templatemerger')    
def templatemerger():    
    return render_template('templatemerger.html')   
  
@app.route('/run-script', methods=['POST'])    
def run_script():    
    global csv_load_count 
        
    csv_file = request.files.get('csv_file')    
    if csv_file:    
        decoded_csv = csv_file.read().decode('utf-8')    
        csv_data = io.StringIO(decoded_csv)    
        df = pd.read_csv(csv_data)    
    
        # Increment the csv_load_count    
        csv_load_count += 1    
    
        # Create the full folder path with index    
        folder_name = f"{datetime.now().strftime('%Y-%m-%d')}({csv_load_count})"    
        full_folder_path = os.path.join(os.path.expanduser('~\\Downloads'), folder_name)    
        if not os.path.exists(full_folder_path):    
            os.makedirs(full_folder_path)    
    
        result = export_images(df, full_folder_path)
        if result.get('error'):    
            return jsonify(result), 400    
   
        return Response(stream_with_context(processing_generator(io.StringIO(decoded_csv), full_folder_path)), mimetype='text/html')    
    else:    
        return jsonify({"error": "CSV file not provided"}), 400    
  
  
if __name__ == '__main__':    
    print("Running Print Layout Lab application... at http://127.0.0.1:5000")    
    app.run(debug=True)