from fontTools.ttLib import TTFont  
from PIL import Image, ImageDraw, ImageFont 
  
def list_supported_glyphs(font_path):  
    font = TTFont(font_path)  
    cmap = font.getBestCmap()  
  
    for code_point, name in cmap.items():  
        print(f"U+{code_point:04X}: {name}")  
  
def replace_last_letter(text, font_to_uni):  
    words = text.split()  
    result = []  
    for word in words:  
        last_letter = word[-1]  
        if last_letter in font_to_uni:  
            word = word[:-1] + chr(int(font_to_uni[last_letter], 16))  
        result.append(word)  
    return ' '.join(result)  
  
def get_text_dimensions(text, font):  
    ascent, descent = font.getmetrics()  
    text_width, text_height = font.getmask(text).getbbox()[2:4]  
    height = text_height + descent  
    return (text_width, height)  
  
def create_image_with_centered_text(text, font_path, font_size, image_size, text_color, bg_color, font_to_uni):  
    # Replace the last letter of each word with the specified Unicode character  
    text = replace_last_letter(text, font_to_uni)  
  
    # Create a PIL font from the font file  
    pil_font = ImageFont.truetype(font_path, font_size)  
  
    image = Image.new('RGB', image_size, color=bg_color)  
    draw = ImageDraw.Draw(image)  
  
    text_width, text_height = get_text_dimensions(text, pil_font)  
  
    x = (image_size[0] - text_width) // 2  
    y = (image_size[1] - text_height) // 2  
  
    draw.text((x, y), text, font=pil_font, fill=text_color)  
    return image  
  
font_path = r"fonts_JEW/Buffalo Nickel.ttf"  
list_supported_glyphs(font_path)  
  
font_to_uni = {  
    "a": "0A01",  
    "b": "0A02",  
    "c": "0A03",  
    "d": "0A04",  
    "e": "0A05",  
    "f": "0A06",

    "g": "0B07",  
    "h": "0B08",  
    "i": "0B09",  
    "j": "0B10",  
    "k": "0B11",  
    "l": "0B12",

    "m": "0C13",  
    "n": "0C14",  
    "o": "0C15",  
    "p": "0C16",  
    "q": "0C17",  
    "r": "0C18",

    "s": "0D19",  
    "t": "0D20",  
    "u": "0D21",  
    "v": "0D22",  
    "w": "0D23",  
    "x": "0D24",

    "y": "0E25",  
    "z": "0E326",  
}  
  
text = "Big Fat Donkey Balls"  
font_size = 30  
image_size = (500, 300)  
text_color = (0, 0, 0)  
bg_color = (255, 255, 255)  
  
image = create_image_with_centered_text(text, font_path, font_size, image_size, text_color, bg_color, font_to_uni)  
image.show()  
