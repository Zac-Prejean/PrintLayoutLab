import os    
import re    
import io    
import csv   
import pandas as pd    
from datetime import datetime   
from flask import Flask, jsonify, render_template, request, Response, stream_with_context    
from PIL import Image, ImageDraw, ImageFont    
from config import color_name_to_rgb    
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
    sku_to_font as nck_sku_to_font,    
    sku_to_fontsize_placement as nck_sku_to_fontsize_placement,
)  
from ring_config import (     
    sku_to_font as rng_sku_to_font,    
    sku_to_fontsize_placement as rng_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as rng_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as rng_sku_to_second_line_font,   
    rng_sku_needs_white_background, rng_sku_to_image_one_line, rng_sku_to_image_two_line,
)  
# Merge dictionaries    
sku_to_image = {**deskplates_sku_to_image, **tumbler_sku_to_image, **nck_sku_to_image}    
sku_to_font = {**deskplates_sku_to_font, **tumbler_sku_to_font, **nck_sku_to_font, **rng_sku_to_font}    
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
        for text, skus in skip_line["line1"].items():    
            if clean_sku in skus:    
                pattern = re.compile(text, flags=re.IGNORECASE)    
                line = pattern.sub('', line).strip()    
    
        for text, skus in skip_line["line2"].items():    
            if clean_sku in skus and line_index == 1:    
                pattern = re.compile(text, flags=re.IGNORECASE)    
                line = pattern.sub('', line).strip()    
    
        processed_line = process_special_rules(clean_sku, line, line_index)
    
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
    
def calculate_font_size_and_placement(sku, text, num_chars):  
    max_x = sku_to_fontsize_placement.get(sku, {}).get("max_x", 3700)  
    if sku.startswith("RNG"):  
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
    
def calculate_second_font_size_and_placement(sku, num_chars):    
    sku_fontsize_placement = sku_to_second_fontsize_placement.get(sku, {})    
    values = sku_fontsize_placement.get(num_chars, (200, None, 100))    
    if len(values) == 2:    
        font_size, y = values    
        x = None    
    else:    
        font_size, x, y = values    
    print(f"Num chars (second line): {num_chars}")    
    return font_size, x, y    
    
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
    
def draw_white_background(draw, x, y, text_width, text_height, margin=-40):    
    draw.rectangle([x - margin, y - margin, x + text_width + margin, y + text_height + margin], fill=(255, 255, 255))  
  
# Process each row from the dataframe    
def process_row(index, row, folder_name):      
    # Extract clean SKU and background image path from the row      
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
    
    match = re.search(r'(?:Personalization|Custom Name):([\s\S]+)', str(item_options))    
    if match:    
        personalization_text = match.group(1)    
    else:    
        personalization_text = ''    
    
    lines = [line for line in personalization_text.split('\n') if line.strip()]    
    lines = [re.sub(r'Line \d+: ?', '', line).strip('\r') for line in lines]    
    lines = [line.strip() for line in lines if line.strip()]    
    
    if not lines:    
        image = create_check_csv_image()    
        image_name = f"{order_number}_{sku}_{index}.png"    
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), image_name)    
        image.save(image_path)    
        print(f"Error: list index out of range, saved {order_number}_{sku}_{index}.png")    
        return    
    else:    
        num_chars_line1 = len(lines[0])

    if clean_sku.startswith("RNG"):  
        num_lines = len(lines)  
        if num_lines == 1:  
            background_image_path = rng_sku_to_image_one_line.get(clean_sku)  
        elif num_lines == 2:  
            background_image_path = rng_sku_to_image_two_line.get(clean_sku)  
        else:  
            background_image_path = None
    
    # Add a check to skip the text specified in the skip_line dictionary    
    skip_text = skip_line.get("skip_line1_text", {}).get(clean_sku)    
    
    if len(lines) > 0:    
        print(f"First line before checking: {lines[0]}")    
    
    if skip_text and len(lines) > 0 and lines[0] == skip_text:    
        lines.pop(0)    
        print(f"First line removed: {lines}")    
    
    # Apply special rules to personalization text and font color    
    processed_text = process_personalization_text(personalization_text, clean_sku)    
    lines = [line for line in processed_text.split('\n') if line.strip()]    
    
    num_chars_line1 = len(lines[0])    
    font_size_line1, x_line1, y_line1 = calculate_font_size_and_placement(clean_sku, lines[0], num_chars_line1)  
    
    
    if len(lines) > 1:    
        num_chars_line2 = len(lines[1])    
        font_size_line2, x_line2, y_line2 = calculate_second_font_size_and_placement(clean_sku, num_chars_line2)      
    else:    
        font_size_line2, x_line2, y_line2 = None, None, None    
    
    # Create image with personalized text    
    image = Image.open(background_image_path) if background_image_path else Image.new('RGB', (3250, 1750), color='white')    
    draw = ImageDraw.Draw(image)    
    image_width, _ = image.size    
    
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
        font_size = font_size_line2 if i == 1 else font_size_line1    
        font = load_font(font_path, font_size)    
    
        text_y = y_line2 if i == 1 else y_line1    
    
        # Only center the text if x-coordinate is not provided    
        if i == 1 and x_line2 is not None:    
            text_x = x_line2    
        elif x_line1 is not None:    
            text_x = x_line1    
        else:    
            left, _, right, _ = font.getbbox(line)    
            text_width = right - left    
            text_x = (image_width - text_width) // 2    
    
        # Draw a white background behind the text if the SKU starts with "RNG"    
        if rng_sku_needs_white_background(clean_sku):    
            left, text_y1, right, text_y2 = font.getbbox(line)    
            text_width = right - left    
            text_height = text_y2 - text_y1    
            draw_white_background(draw, text_x, text_y, text_width, text_height)    
              
        # Draw the current line    
        draw.text((text_x, text_y), line, fill=processed_font_color, font=font)    
    
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
   
  
    
def processing_generator(csv_data, folder_name):  
  
    # Read the CSV data using the csv module    
    csv_reader = csv.DictReader(csv_data)    
    rows = [row for row in csv_reader]    
    
    # Convert the CSV data to a dataframe    
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