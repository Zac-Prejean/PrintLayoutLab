import os  

sku_to_image = { 

    "NCKGLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless.png'),
    "NCK02GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless.png'),
    "NCK03GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless.png'),
}

sku_to_font = { 

    "NCKGLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Fairy4.5.otf'), 
    "NCK02GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Fairy4.5.otf'),   
    "NCK03GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Fairy4.5.otf'),
}

sku_to_fontsize_placement = {
    "NCKGLDCHN01": {   
        1: (580, 77),  2: (580, 77),  3: (580, 77),  4: (580, 77),  5: (580, 77),  
        6: (450, 70),  7: (580, 77),  8: (580, 77),  9: (580, 77), 10: (580, 77),  
       11: (580, 77), 12: (580, 77), 13: (580, 77), 14: (580, 77), 15: (580, 77),  
       16: (580, 77), 17: (580, 77), 18: (580, 77), 19: (580, 77), 20: (580, 77),  
    },
    "NCK02GLDCHN01": {  
        1: (580, 77),  2: (580, 77),  3: (580, 77),  4: (580, 77),  5: (580, 77),  
        6: (580, 77),  7: (580, 77),  8: (580, 77),  9: (580, 77), 10: (580, 77),  
       11: (580, 77), 12: (580, 77), 13: (580, 77), 14: (580, 77), 15: (580, 77),  
       16: (580, 77), 17: (580, 77), 18: (580, 77), 19: (580, 77), 20: (580, 77),  
    },
    "NCK03GLDCHN01": {    
        1: (580, 77),  2: (580, 77),  3: (580, 77),  4: (580, 77),  5: (580, 77),  
        6: (580, 77),  7: (580, 77),  8: (580, 77),  9: (580, 77), 10: (580, 77),  
       11: (580, 77), 12: (580, 77), 13: (580, 77), 14: (580, 77), 15: (580, 77),  
       16: (580, 77), 17: (580, 77), 18: (580, 77), 19: (580, 77), 20: (580, 77),  
    },
}