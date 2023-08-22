import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))  
background_image_path = os.path.join(script_dir, 'backgrown', 'tumblers', 'UVPPSSCCPTUVP.png')  

sku_to_image = {

    # tumblers
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSCCPTUVP.png'),
    'UVPJMHDBSUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMHDBSUVP.png'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPICBFUVP.png'),
    'UVPPSAIRATTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSAIRATTBUVP.png'),
    'UVPRADENTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPRADENTUVP.png'),
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),

    'UVPANWHTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPANWHTUVP.png'),
    'UVPPSTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSKFGPUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSKFGPUVP.png'),
    'UVPPSKFGWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSKFGWUVP.png'),

    'UVPPSDENTTELUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSDENTTELUVP.png'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),  
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    
    'UVPUYSTD1UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD1UVP.png'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD2UVP.png'),  
    'UVPUYSTD3UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD3UVP.png'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD4UVP.png'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD5UVP.png'),  
    'UVPUYSTD6UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD6UVP.png'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPUYSTD7UVP.png'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSAPPTUVP.png'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSABCTUVP.png'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPENTUVP.png'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSBUSTUVP.png'),

    'UVPJMKTDSUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTDSUVP.png'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTMTUVP.png'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTPCUVP.png'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPJMKTUCUVP.png'),

    'UVPPSB16BUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPHRMBUVP.png'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSPHRMWUVP.png'),
    'UVPPSSTILGBHUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSSTILGWHUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPJMSLCLBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPJMSLCLWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSNUBRBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSNUBRBUVP.png'),
    'UVPPSNUBRWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSNUBRWUVP.png'),

    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSEITTTSBUVP.png'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSEITTTSWUVP.png'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTBUVP.png'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTWUVP.png'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTABUVP.png'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTPTAWUVP.png'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTBUVP.png'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTWUVP.png'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTABUVP.png'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSTTOTAWUVP.png'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSLPTBUVP.png'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSSLPTWUVP.png'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSOPTTBUVP.png'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSOPTTWUVP.png'),

    'UVPPSVETTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSVETTBUVP.png'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', 'UVPPSVETTWUVP.png'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'Backgrown', 'Tumblers', '_blank.png'),
}  

sku_to_font = {

    # tumblers
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'), 
    'UVPJMHDBSUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSAIRATTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPRADENTUVP': os.path.join(script_dir, 'Fonts', 'Brooke Smith Script.ttf'),
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'Fonts', 'Versailles LT Regular.ttf'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),

    'UVPANWHTUVP': os.path.join(script_dir, 'Fonts', 'Rumba.ttf'),
    'UVPPSTBUVP': os.path.join(script_dir, 'Fonts', 'Breathing Regular.ttf'),
    'UVPPSKFGPUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKFGWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),

    'UVPPSDENTTELUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    
    'UVPUYSTD1UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD3UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD6UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPJMKTDSUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),

    'UVPPSB16BUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSTILGBHUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSSTILGWHUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMSLCLBUVP': os.path.join(script_dir, 'Fonts', 'Shorelines Script Bold.otf'),
    'UVPJMSLCLWUVP': os.path.join(script_dir, 'Fonts', 'Shorelines Script Bold.otf'),
    'UVPPSNUBRBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSNUBRWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    'UVPPSVETTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'Fonts', 'Radley-Regular.ttf'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'Fonts', 'Radley-Regular.ttf'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'Fonts', 'BrimNarrow-Combined.ttf'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'Fonts', 'BrimNarrow-Combined.ttf'),
}

sku_to_second_line_font = { 
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'Fonts', 'Calibri-Heart.ttf'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'Fonts', 'Calibri-Heart.ttf'),

    'UVPPSVETTBUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
}

skip_line = {  
    "line1": {  
    "physical therapist": [  
        "UVPPSTTPTBUVP", "UVPPSTTPTWUVP",  
    ],  
    "physical therapist assistant": [  
        "UVPPSTTPTABUVP", "UVPPSTTPTAWUVP",  
    ],  
    "occupational therapist": [  
        "UVPPSTTOTBUVP", "UVPPSTTOTWUVP",  
    ],  
    "occupational therapist assistant": [  
        "UVPPSTTOTABUVP", "UVPPSTTOTAWUVP",  
    ],  
    "speech-language pathologist": [  
        "UVPPSSLPTBUVP", "UVPPSSLPTWUVP",  
    ],  
    },  
    "line2": {  
        "physical therapist": [  
            "UVPPSTTPTBUVP", "UVPPSTTPTWUVP",  
        ],  
        "physical therapist assistant": [  
            "UVPPSTTPTABUVP", "UVPPSTTPTAWUVP",  
        ],  
        "occupational therapist": [  
            "UVPPSTTOTBUVP", "UVPPSTTOTWUVP",  
        ],  
        "occupational therapist assistant": [  
            "UVPPSTTOTABUVP", "UVPPSTTOTAWUVP",  
        ],  
        "speech-language pathologist": [  
            "UVPPSSLPTBUVP", "UVPPSSLPTWUVP",  
        ], 
    },  
} 

# force black font color 
def process_font_color(font_color, clean_sku):  
    if clean_sku in ["UVPPSNUBRBUVP", "UVPPSTTPTBUVP", "UVPPSTTPTABUVP", "UVPPSTTOTBUVP", 
                     "UVPPSTTOTABUVP", "UVPPSSLPTBUVP", "UVPPSOPTTBUVP"]:  
        font_color = (0, 0, 0)  
    return font_color  
  
sku_to_fontsize_placement = {  # (font-size, x, y)  


    #  tumblers 
    'UVPPSSCCPTUVP': {     
         1: (600, 500),  2: (600, 500),  3: (600, 500),  4: (600, 500),  5: (600, 500),  
         6: (600, 500),  7: (600, 500),  8: (600, 500),  9: (600, 500), 10: (600, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPJMHDBSUVP': {       
         1: (425, 1200, 500),  2: (425, 1200, 500),  3: (425, 1200, 500),  4: (425, 1200, 500),  5: (425, 1200, 500),   
         6: (425, 1200, 500),  7: (425, 1200, 500),  8: (425, 1200, 500),  9: (425, 1200, 500), 10: (425, 1200, 500), 
        11: (325, 1200, 600), 12: (325, 1200, 600), 13: (325, 1200, 600), 14: (325, 1200, 600), 15: (325, 1200, 600), 
        16: (325, 1200, 600), 17: (325, 1200, 600), 18: (325, 1200, 600), 19: (325, 1200, 600), 20: (500, 1200, 600),
    },
    'UVPPSPICBFUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },
    'UVPPSAIRATTBUVP': {     
         1: (400, 1000),  2: (400, 1000),  3: (400, 1000),  4: (400, 1000),  5: (400, 1000),  
         6: (400, 1000),  7: (400, 1100),  8: (400, 1100),  9: (400, 1100), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (300, 1200), 14: (300, 1200), 15: (250, 1250), 
        16: (250, 1250), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPRADENTUVP': {     
         1: (700, 500),  2: (700, 500),  3: (700, 500),  4: (700, 500),  5: (700, 500),  
         6: (700, 500),  7: (700, 500),  8: (700, 500),  9: (700, 500), 10: (700, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPPSGKNTPUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPPSGKNTSUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    
    'UVPANWHTUVP': {     
         1: (800, 400), 2: (800, 400), 3: (800, 400), 4: (800, 400), 5: (800, 400),  
         6: (800, 400), 7: (800, 400), 8: (800, 300, 400),  9: (800, 300, 400), 10: (800, 300, 400),  
        11: (800, 200, 400), 12: (800, 200, 400), 13: (800, 200, 400), 14: (800, 200, 400), 15: (800, 200, 400), 
        16: (800, 100, 400), 17: (800, 100, 400), 18: (800, 100, 400), 19: (800, 100, 400), 20: (800, 100, 400),
    },
    'UVPPSTBUVP': {     
         1: (800, 100), 2: (800, 100), 3: (800, 100), 4: (800, 100), 5: (800, 100),  
         6: (800, 100), 7: (600, 200), 8: (600, 200),  9: (600, 200), 10: (600, 200),  
        11: (400, 300), 12: (400, 300), 13: (400, 300), 14: (400, 300), 15: (300, 400), 
        16: (300, 400), 17: (300, 400), 18: (250, 400), 19: (250, 400), 20: (250, 400),
    },
    'UVPPSKFGPUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 300), 5: (800, 300),  
         6: (800, 300), 7: (800, 300), 8: (800, 300, 300),  9: (800, 300, 300), 10: (800, 300, 300),  
        11: (800, 200, 300), 12: (700, 200, 400), 13: (700, 200, 400), 14: (600, 200, 500), 15: (600, 200, 500), 
        16: (600, 100, 500), 17: (500, 100, 500), 18: (500, 100, 500), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSKFGWUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 300), 5: (800, 300),  
         6: (800, 300), 7: (800, 300), 8: (800, 300, 300),  9: (800, 300, 300), 10: (800, 300, 300),  
        11: (800, 200, 300), 12: (700, 200, 400), 13: (700, 200, 400), 14: (600, 200, 500), 15: (600, 200, 500), 
        16: (600, 100, 500), 17: (500, 100, 500), 18: (500, 100, 500), 19: (400, 100, 600), 20: (400, 100, 600),
    },

    'UVPPSDENTTELUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSDENTBLKUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSDENTPNKUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSKIDTBUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },
    'UVPPSKIDTWUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },
    'UVPPSKIDTPUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },
    'UVPUYSTD1UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD2UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 800, 500), 9: (650, 750, 500), 10: (650, 700, 500),  
       11: (650, 550, 500), 12: (600, 400, 500), 13: (500, 550, 600), 14: (500, 600, 600), 15: (500, 350, 600), 
       16: (500, 200, 600), 17: (400, 500, 650), 18: (400, 500, 650), 19: (400, 650), 20: (400, 650),
    },   
    'UVPUYSTD3UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    },  
    'UVPUYSTD4UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD5UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD6UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 800, 500), 9: (650, 750, 500), 10: (650, 700, 500),  
       11: (650, 550, 500), 12: (600, 400, 500), 13: (500, 550, 600), 14: (500, 600, 600), 15: (500, 350, 600), 
       16: (500, 200, 600), 17: (400, 500, 650), 18: (400, 500, 650), 19: (400, 650), 20: (400, 650),
    },  
    'UVPUYSTD7UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 

    'UVPPSAPPTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSABCTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSPENTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSBUSTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },

    'UVPJMKTDSUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 900, 300), 5: (800, 700, 300),  
         6: (800, 500, 300),  7: (800, 300, 300),  8: (700, 100, 400),  9: (700, 100, 400), 10: (600, 200, 450),  
        11: (600, 100, 450), 12: (500, 200, 500), 13: (500, 100, 500), 14: (450, 200, 550), 15: (450, 100, 550), 
        16: (400, 200, 550), 17: (350, 100, 600), 18: (350, 100, 600), 19: (300, 100, 650), 20: (300, 100, 650),
    },
    'UVPJMKTMTUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 900, 300), 5: (800, 700, 300),  
         6: (800, 500, 300),  7: (800, 300, 300),  8: (700, 100, 400),  9: (700, 100, 400), 10: (600, 200, 450),  
        11: (600, 100, 450), 12: (500, 200, 500), 13: (500, 100, 500), 14: (450, 200, 550), 15: (450, 100, 550), 
        16: (400, 200, 550), 17: (350, 100, 600), 18: (350, 100, 600), 19: (300, 100, 650), 20: (300, 100, 650),
    },
    'UVPJMKTPCUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 900, 400), 4: (700, 800, 400), 5: (700, 400, 400),  
         6: (700, 300, 400),  7: (700, 100, 400),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 200, 550),  
        11: (500, 100, 550), 12: (400, 200, 600), 13: (400, 100, 600), 14: (350, 200, 650), 15: (350, 100, 650), 
        16: (300, 200, 700), 17: (300, 100, 700), 18: (300, 100, 700), 19: (250, 100, 750), 20: (250, 100, 750),
    },
    'UVPJMKTUCUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 900, 300), 5: (800, 700, 300),  
         6: (800, 500, 300),  7: (800, 300, 300),  8: (700, 100, 400),  9: (700, 100, 400), 10: (600, 200, 450),  
        11: (600, 100, 450), 12: (500, 200, 500), 13: (500, 100, 500), 14: (450, 200, 550), 15: (450, 100, 550), 
        16: (400, 200, 550), 17: (350, 100, 600), 18: (350, 100, 600), 19: (300, 100, 650), 20: (300, 100, 650),
    },

    'UVPPSB16BUVP': {     
         1: (700, 200, 300),  2: (700, 200, 300),  3: (700, 200, 300),  4: (700, 200, 300),  5: (700, 200, 300),  
         6: (700, 200, 300),  7: (700, 200, 300),  8: (700, 200, 300),  9: (700, 200, 300), 10: (700, 200, 300),  
        11: (600, 200, 400), 12: (550, 200, 450), 13: (500, 200, 500), 14: (500, 200, 500), 15: (400, 200, 600), 
        16: (400, 200, 600), 17: (400, 200, 600), 18: (400, 200, 600), 19: (300, 200, 700), 20: (300, 200, 700),
    },
    'UVPPSB16WUVP': {     
         1: (700, 200, 300),  2: (700, 200, 300),  3: (700, 200, 300),  4: (700, 200, 300),  5: (700, 200, 300),  
         6: (700, 200, 300),  7: (700, 200, 300),  8: (700, 200, 300),  9: (700, 200, 300), 10: (700, 200, 300),  
        11: (600, 200, 400), 12: (550, 200, 450), 13: (500, 200, 500), 14: (500, 200, 500), 15: (400, 200, 600), 
        16: (400, 200, 600), 17: (400, 200, 600), 18: (400, 200, 600), 19: (300, 200, 700), 20: (300, 200, 700),
    },
    'UVPPSTTUMBUVP': {     
         1: (200, 875),  2: (200, 875),  3: (200, 875),  4: (200, 875),  5: (200, 875),  
         6: (200, 875),  7: (200, 875),  8: (200, 875),  9: (200, 875), 10: (200, 875),  
        11: (200, 875), 12: (200, 875), 13: (200, 875), 14: (200, 875), 15: (200, 875), 
        16: (200, 875), 17: (200, 875), 18: (200, 875), 19: (200, 875), 20: (200, 875),
        21: (200, 875), 22: (200, 875), 23: (200, 875), 24: (200, 875), 25: (200, 875), 
    },
    'UVPPSTTUMWUVP': {     
         1: (200, 875),  2: (200, 875),  3: (200, 875),  4: (200, 875),  5: (200, 875),  
         6: (200, 875),  7: (200, 875),  8: (200, 875),  9: (200, 875), 10: (200, 875),  
        11: (200, 875), 12: (200, 875), 13: (200, 875), 14: (200, 875), 15: (200, 875), 
        16: (200, 875), 17: (200, 875), 18: (200, 875), 19: (200, 875), 20: (200, 875),
        21: (200, 875), 22: (200, 875), 23: (200, 875), 24: (200, 875), 25: (200, 875), 
    },
    'UVPPSPHRMBUVP': {     
         1: (700, 1000, 300),  2: (700, 1000, 300),  3: (700, 1000, 300),  4: (700, 1000, 300),  5: (700, 1000, 300),  
         6: (700, 1000, 300),  7: (700, 1000, 300),  8: (600, 1000, 400),  9: (600, 1000, 400), 10: (600, 1000, 400),  
        11: (500, 1000, 450), 12: (400, 1000, 500), 13: (400, 1000, 500), 14: (400, 1000, 500), 15: (300, 1000, 600), 
        16: (300, 1000, 600), 17: (300, 1000, 600), 18: (300, 1000, 600), 19: (250, 1000, 700), 20: (250, 1000, 700),
    },
    'UVPPSPHRMWUVP': {     
         1: (700, 1000, 300),  2: (700, 1000, 300),  3: (700, 1000, 300),  4: (700, 1000, 300),  5: (700, 1000, 300),  
         6: (700, 1000, 300),  7: (700, 1000, 300),  8: (600, 1000, 400),  9: (600, 1000, 400), 10: (600, 1000, 400),  
        11: (500, 1000, 450), 12: (400, 1000, 500), 13: (400, 1000, 500), 14: (400, 1000, 500), 15: (300, 1000, 600), 
        16: (300, 1000, 600), 17: (300, 1000, 600), 18: (300, 1000, 600), 19: (250, 1000, 700), 20: (250, 1000, 700),
    },
    'UVPPSSTILGBHUVP': {     
         1: (700, 100, 400),  2: (700, 100, 400),  3: (700, 100, 400),  4: (700, 100, 400),  5: (700, 100, 400),  
         6: (700, 100, 400),  7: (600, 100, 500),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 100, 600),  
        11: (500, 100, 600), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700), 
        16: (350, 100, 750), 17: (350, 100, 750), 18: (350, 100, 750), 19: (300, 100, 800), 20: (300, 100, 800),
        21: (300, 100, 800), 22: (200, 100, 900), 23: (200, 100, 900), 24: (200, 100, 900), 25: (200, 100, 900),
    },
    'UVPPSSTILGWHUVP': {     
         1: (700, 100, 400),  2: (700, 100, 400),  3: (700, 100, 400),  4: (700, 100, 400),  5: (700, 100, 400),  
         6: (700, 100, 400),  7: (600, 100, 500),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 100, 600),  
        11: (500, 100, 600), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700), 
        16: (350, 100, 750), 17: (350, 100, 750), 18: (350, 100, 750), 19: (300, 100, 800), 20: (300, 100, 800),
        21: (300, 100, 800), 22: (200, 100, 900), 23: (200, 100, 900), 24: (200, 100, 900), 25: (200, 100, 900),
    },
    'UVPJMSLCLBUVP': {     
         1: (400, 400),  2: (400, 400),  3: (400, 400),  4: (400, 400),  5: (400, 400),  
         6: (400, 400),  7: (300, 500),  8: (300, 500),  9: (300, 500), 10: (300, 600),  
        11: (300, 600), 12: (250, 700), 13: (250, 700), 14: (250, 700), 15: (250, 700), 
        16: (250, 750), 17: (250, 750), 18: (250, 750), 19: (200, 800), 20: (200, 800),
        21: (200, 800), 22: (200, 900), 23: (200, 900), 24: (200, 900), 25: (200, 900),
    },
    'UVPJMSLCLWUVP': {     
         1: (400, 400),  2: (400, 400),  3: (400, 400),  4: (400, 400),  5: (400, 400),  
         6: (400, 400),  7: (300, 500),  8: (300, 500),  9: (300, 500), 10: (300, 600),  
        11: (300, 600), 12: (250, 700), 13: (250, 700), 14: (250, 700), 15: (250, 700), 
        16: (250, 750), 17: (250, 750), 18: (250, 750), 19: (200, 800), 20: (200, 800),
        21: (200, 800), 22: (200, 900), 23: (200, 900), 24: (200, 900), 25: (200, 900),
    },
    'UVPPSNUBRBUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },
    'UVPPSNUBRWUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },

    'UVPPSEITTTSBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (300, 1300), 
        16: (250, 1300), 17: (250, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSEITTTSWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTABUVP':{     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTAWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (300, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTABUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTAWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSSLPTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSSLPTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSOPTTBUVP': {     
         1: (400, 2500),  2: (400, 2500),  3: (400, 2500),  4: (400, 2500),  5: (400, 2500),  
         6: (400, 2500),  7: (400, 2500),  8: (400, 2500),  9: (400, 2500), 10: (300, 2500),  
        11: (300, 2500), 12: (300, 2500), 13: (300, 2500), 14: (300, 2500), 15: (250, 2500), 
        16: (250, 2500), 17: (200, 2500), 18: (200, 2500), 19: (150, 2500), 20: (150, 2500),
    },
    'UVPPSOPTTWUVP': {     
         1: (400, 2500),  2: (400, 2500),  3: (400, 2500),  4: (400, 2500),  5: (400, 2500),  
         6: (400, 2500),  7: (400, 2500),  8: (400, 2500),  9: (400, 2500), 10: (300, 2500),  
        11: (300, 2500), 12: (300, 2500), 13: (300, 2500), 14: (300, 2500), 15: (250, 2500), 
        16: (250, 2500), 17: (200, 2500), 18: (200, 2500), 19: (150, 2500), 20: (150, 2500),
    },

    'UVPPSVETTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSVETTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPCCGTUMBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPCCGTUMWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPJMMAMATBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (800, 300),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPJMMAMATWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (800, 300),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPPSAUNTTBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (700, 400),  
         6: (700, 400),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (450, 550),  
        11: (450, 550), 12: (400, 600), 13: (350, 650), 14: (300, 650), 15: (300, 650), 
        16: (300, 650), 17: (250, 700), 18: (250, 700), 19: (200, 750), 20: (200, 750),
    },
    'UVPPSAUNTTWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (700, 400),  
         6: (700, 400),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (450, 550),  
        11: (450, 550), 12: (400, 600), 13: (350, 650), 14: (300, 650), 15: (300, 650), 
        16: (300, 650), 17: (250, 700), 18: (250, 700), 19: (200, 750), 20: (200, 750),
    },
    
 }


sku_to_second_fontsize_placement = {  # (font-size, x, y)

    #  tumblers 
    'UVPPSGKNTPUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSGKNTSUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },

    'UVPPSKFGPUVP': {     
         1: (600, 300), 2: (600, 300), 3: (600, 300), 4: (600, 300), 5: (600, 300),  
         6: (600, 300), 7: (600, 300), 8: (600, 300, 300),  9: (600, 300, 300), 10: (600, 300, 300),  
        11: (500, 200, 300), 12: (500, 200, 400), 13: (500, 200, 400), 14: (400, 200, 500), 15: (400, 200, 500), 
        16: (400, 100, 500), 17: (300, 100, 500), 18: (300, 100, 500), 19: (200, 100, 600), 20: (200, 100, 600),
    },
    'UVPPSKFGWUVP': {     
         1: (600, 300), 2: (600, 300), 3: (600, 300), 4: (600, 300), 5: (600, 300),  
         6: (600, 300), 7: (600, 300), 8: (600, 300, 300),  9: (600, 300, 300), 10: (600, 300, 300),  
        11: (500, 200, 300), 12: (500, 200, 400), 13: (500, 200, 400), 14: (400, 200, 500), 15: (400, 200, 500), 
        16: (400, 100, 500), 17: (300, 100, 500), 18: (300, 100, 500), 19: (200, 100, 600), 20: (200, 100, 600),
    },

    'UVPPSVETTBUVP': {     
         1: (300, 2100),  2: (300, 2100),  3: (300, 2100),  4: (300, 2100),  5: (300, 2100),  
         6: (300, 2100),  7: (300, 2100),  8: (300, 2100),  9: (300, 2100), 10: (200, 2100),  
        11: (200, 2100), 12: (200, 2100), 13: (200, 2100), 14: (200, 2100), 15: (150, 2100), 
        16: (150, 2100), 17: (100, 2100), 18: (100, 2100), 19: (50, 2100),  20: (50, 2100),
    },
    'UVPPSVETTWUVP': {     
         1: (300, 2100),  2: (300, 2100),  3: (300, 2100),  4: (300, 2100),  5: (300, 2100),  
         6: (300, 2100),  7: (300, 2100),  8: (300, 2100),  9: (300, 2100), 10: (200, 2100),  
        11: (200, 2100), 12: (200, 2100), 13: (200, 2100), 14: (200, 2100), 15: (150, 2100), 
        16: (150, 2100), 17: (100, 2100), 18: (100, 2100), 19: (50, 2100),  20: (50, 2100),
    },
    'UVPCCGTUMBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPCCGTUMWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPJMMAMATBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPJMMAMATWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSAUNTTBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSAUNTTWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
 }


   
