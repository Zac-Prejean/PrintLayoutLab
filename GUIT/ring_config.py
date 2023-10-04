import os  
  
def handle_rng_skus(clean_sku, lines, rng_sku_to_image_one_line, rng_sku_to_image_two_line, original_background_image_path):  
    if not clean_sku.startswith("RNG"):  
        return original_background_image_path  
  
    if len(lines) == 1:  
        background_image_path = rng_sku_to_image_one_line.get(clean_sku, None)  
    elif len(lines) == 2:  
        background_image_path = rng_sku_to_image_two_line.get(clean_sku, None)  
    else:  
        background_image_path = None  
  
    return background_image_path

def draw_white_background_if_needed(clean_sku, rng_sku_needs_white_background, font, line, text_x, text_y, draw_white_background, draw):  
    if rng_sku_needs_white_background(clean_sku):  
        left, text_y1, right, text_y2 = font.getbbox(line)  
        text_width = right - left  
        text_height = text_y2 - text_y1  
        draw_white_background(draw, text_x, text_y, text_width, text_height)  


rng_sku_to_image_two_line = { 

    "RNG35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNG35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),     
    "RNG35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),    
    "RNGDBL35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),    
    "RNGDBL35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),     
    "RNGDBL35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),    

    "RNG46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNG46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),     
    "RNG46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),    
    "RNGDBL46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),    
    "RNGDBL46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),     
    "RNGDBL46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'), 

    "RNG68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNG68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),
    "RNG68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),
    "RNGDBL68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'), 
    "RNGDBL68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNGDBL68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),

    "RNG78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'), 
    "RNG78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNG78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),
    "RNGDBL78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'), 
    "RNGDBL78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),  
    "RNGDBL78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size-DBL.png'),

    "RNG910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),  
    "RNG910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),  
    "RNG910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),   
    "RNGDBL910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),   
    "RNGDBL910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),    
    "RNGDBL910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'), 

    "RNG911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),  
    "RNG911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),  
    "RNG911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),   
    "RNGDBL911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),   
    "RNGDBL911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'),    
    "RNGDBL911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11-DBL.png'), 
} 

rng_sku_to_image_one_line = { 

    "RNG35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNG35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNG35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),
    "RNGDBL35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNGDBL35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNGDBL35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),

    "RNG46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNG46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNG46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),
    "RNGDBL46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNGDBL46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),  
    "RNGDBL46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size4-6.png'),

    "RNG68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNG68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNG68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),
    "RNGDBL68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNGDBL68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNGDBL68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),

    "RNG78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNG78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNG78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),
    "RNGDBL78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNGDBL78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),  
    "RNGDBL78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size7-8.png'),

    "RNG910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNG910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNG910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNGDBL910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),   
    "RNGDBL910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),    
    "RNGDBL910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),

    "RNG911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNG911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNG911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),  
    "RNGDBL911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),   
    "RNGDBL911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),    
    "RNGDBL911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'size9-11.png'),

} 

sku_to_font = { 

    "RNG35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNG35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNGDBL35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

    "RNG46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNG46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNGDBL46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

    "RNG68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

    "RNG78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNG78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNGDBL78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

    "RNG910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNG910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

    "RNG911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNG911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),  
    "RNG911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 
    "RNGDBL911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'),   
    "RNGDBL911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyTop1.4.otf'), 

} 

sku_to_second_line_font = {  

    "RNG35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNG35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL35GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNGDBL35SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL35RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

    "RNG46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNG46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL46GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNGDBL46SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL46RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

    "RNG68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL68GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL68SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL68RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

    "RNG78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNG78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL78GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL78SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNGDBL78RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

    "RNG910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNG910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL910GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL910SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL910RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

    "RNG911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNG911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),  
    "RNG911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 
    "RNGDBL911GLD": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL911SIL": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'),   
    "RNGDBL911RSG": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'ShelbyBottom.ttf'), 

} 

sku_to_fontsize_placement = {
     # size 4-6 
    "RNG35GLD": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG35SIL": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG35RSG": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL35GLD": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    }, 
    "RNGDBL35SIL": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL35RSG": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },

    "RNG46GLD": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG46SIL": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG46RSG": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL46GLD": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    }, 
    "RNGDBL46SIL": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL46RSG": {  
       "max_x": 3225,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },

    # size 7-8
    "RNG68GLD": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG68SIL": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG68RSG": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL68GLD": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL68SIL": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL68RSG": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },

    "RNG78GLD": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG78SIL": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG78RSG": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL78GLD": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL78SIL": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL78RSG": {  
        "max_x": 3485,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },

    # size 9-11
    "RNG910GLD": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG910SIL": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG910RSG": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL910GLD": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL910SIL": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL910RSG": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },

    "RNG911GLD": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG911SIL": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNG911RSG": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL911GLD": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL911SIL": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    "RNGDBL911RSG": {  
       "max_x": 3520,  
        1: (580, None, 77),  2: (580, None, 77),  3: (580, None, 77),  4: (580, None, 77),  5: (580, None, 77),  
        6: (580, None, 77),  7: (580, None, 77),  8: (580, None, 77),  9: (580, None, 77), 10: (580, None, 77),  
       11: (580, None, 77), 12: (580, None, 77), 13: (580, None, 77), 14: (580, None, 77), 15: (580, None, 77),  
       16: (580, None, 77), 17: (580, None, 77), 18: (580, None, 77), 19: (580, None, 77), 20: (580, None, 77),  
    },
    
} 

sku_to_second_fontsize_placement = { 
    
    # size 4-6
    "RNG35GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG35SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG35RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL35GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL35SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL35RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },

    "RNG46GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG46SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG46RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL46GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL46SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL46RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },

    # size 7-8
    "RNG68GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG68SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG68RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL68GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL68SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL68RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },

    "RNG78GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG78SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNG78RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL78GLD": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL78SIL": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },
    "RNGDBL78RSG": {  
        1: (580, 440, 77),  2: (580, 440, 77),  3: (580, 440, 77),  4: (580, 440, 77),  5: (580, 440, 77),  
        6: (580, 440, 77),  7: (580, 440, 77),  8: (580, 440, 77),  9: (580, 440, 77), 10: (580, 440, 77), 
       11: (580, 440, 77), 12: (580, 440, 77), 13: (580, 440, 77), 14: (580, 440, 77), 15: (580, 440, 77),  
       16: (580, 440, 77), 17: (580, 440, 77), 18: (580, 440, 77), 19: (580, 440, 77), 20: (580, 440, 77),  
    },


    # size 9-11
    "RNG910GLD": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNG910SIL": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNG910RSG": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL910GLD": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL910SIL": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL910RSG": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },

    "RNG911GLD": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNG911SIL": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNG911RSG": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL911GLD": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL911SIL": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },
    "RNGDBL911RSG": {  
        1: (580, 310, 77),  2: (580, 310, 77),  3: (580, 310, 77),  4: (580, 310, 77),  5: (580, 310, 77),  
        6: (580, 310, 77),  7: (580, 310, 77),  8: (580, 310, 77),  9: (580, 310, 77), 10: (580, 310, 77), 
       11: (580, 310, 77), 12: (580, 310, 77), 13: (580, 310, 77), 14: (580, 310, 77), 15: (580, 310, 77),  
       16: (580, 310, 77), 17: (580, 310, 77), 18: (580, 310, 77), 19: (580, 310, 77), 20: (580, 310, 77),  
    },    
}  
   
def rng_sku_needs_white_background(clean_sku):  
    return clean_sku.startswith("RNG")

