import os  


sku_to_image = { 

    "NCKGLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-1ln.png'),
    "NCK02GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-2ln.png'),
    "NCK03GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-3ln.png'),
    "NCK04GLDCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-4ln.png'),
    "NCKSILCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-1ln.png'),
    "NCK02SILCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-2ln.png'),
    "NCK03SILCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-3ln.png'),
    "NCK04SILCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-4ln.png'),
    "NCKRSGCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-1ln.png'),
    "NCK02RSGCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-2ln.png'),
    "NCK03RSGCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-3ln.png'),
    "NCK04RSGCHN01": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'jewlery', 'neckless-4ln.png'),

}

design_to_font = { 

    "Al Libretto": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Allibretto.ttf'), 
    "Bella": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Bella.ttf'),   
    "Buffalo Nickel": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Buffalo Nickel.ttf'),
    "Cervantiss": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Cervantiss.ttf'),
    "Claster Regular": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Claster Regular.ttf'), 
    "Fairy-Bold": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Fairy-Bold.ttf'),   
    "Nella Sue": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Fairy-Bold.ttf'),   
    "Autumn Chant": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Mon Amour.ttf'),
    "Mon Amour": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'Mon Amour.ttf'),
    "UKIJ": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts_JEW', 'UKIJ.ttf'),
}

sku_to_fontsize_placement = {
    "Al Libretto": {   
        1: (430, 100),  2: (430, 100),  3: (430, 100),  4: (430, 100),  5: (430, 100),  
        6: (430, 100),  7: (430, 100),  8: (430, 100),  9: (430, 100), 10: (430, 100),  
       11: (430, 100), 12: (430, 100), 13: (430, 100), 14: (430, 100), 15: (430, 100),  
       16: (430, 100), 17: (430, 100), 18: (430, 100), 19: (430, 100), 20: (430, 100),  
    },
    "Bella": {  
        1: (650, 90),  2: (650, 90),  3: (650, 90),  4: (650, 90),  5: (650, 90),  
        6: (650, 90),  7: (650, 90),  8: (650, 90),  9: (650, 90), 10: (650, 90),  
       11: (650, 90), 12: (650, 90), 13: (650, 90), 14: (650, 90), 15: (650, 90),  
       16: (650, 90), 17: (650, 90), 18: (650, 90), 19: (650, 90), 20: (650, 90),  
    },
    "Buffalo Nickel": {    
        1: (500, 90),  2: (500, 90),  3: (500, 90),  4: (500, 90),  5: (500, 90),  
        6: (500, 90),  7: (500, 90),  8: (500, 90),  9: (500, 90), 10: (500, 90),  
       11: (500, 90), 12: (500, 90), 13: (500, 90), 14: (500, 90), 15: (500, 90),  
       16: (500, 90), 17: (500, 90), 18: (500, 90), 19: (500, 90), 20: (500, 90),  
    },
    "Cervantiss": {    
        1: (620, 0),  2: (620, 0),  3: (620, 0),  4: (620, 0),  5: (620, 0),  
        6: (620, 0),  7: (620, 0),  8: (620, 0),  9: (620, 0), 10: (620, 0),  
       11: (620, 0), 12: (620, 0), 13: (620, 0), 14: (620, 0), 15: (620, 0),  
       16: (620, 0), 17: (620, 0), 18: (620, 0), 19: (620, 0), 20: (620, 0),  
    },
    "Claster Regular": {    
        1: (640, -150),  2: (640, -150),  3: (640, -150),  4: (640, -150),  5: (640, -150),  
        6: (640, -150),  7: (640, -150),  8: (640, -150),  9: (640, -150), 10: (640, -150),  
       11: (640, -150), 12: (640, -150), 13: (640, -150), 14: (640, -150), 15: (640, -150),  
       16: (640, -150), 17: (640, -150), 18: (640, -150), 19: (640, -150), 20: (640, -150),  
    },
    "Fairy-Bold": {    
        1: (500, -10),  2: (500, -10),  3: (500, -10),  4: (500, -10),  5: (500, -10),  
        6: (500, -10),  7: (500, -10),  8: (500, -10),  9: (500, -10), 10: (500, -10),  
       11: (500, -10), 12: (500, -10), 13: (500, -10), 14: (500, -10), 15: (500, -10),  
       16: (500, -10), 17: (500, -10), 18: (500, -10), 19: (500, -10), 20: (500, -10),  
    },
    "Nella Sue": {    
        1: (500, -10),  2: (500, -10),  3: (500, -10),  4: (500, -10),  5: (500, -10),  
        6: (500, -10),  7: (500, -10),  8: (500, -10),  9: (500, -10), 10: (500, -10),  
       11: (500, -10), 12: (500, -10), 13: (500, -10), 14: (500, -10), 15: (500, -10),  
       16: (500, -10), 17: (500, -10), 18: (500, -10), 19: (500, -10), 20: (500, -10),  
    },
    "Autumn Chant": {    
        1: (480, 50),  2: (480, 50),  3: (480, 50),  4: (480, 50),  5: (480, 50),  
        6: (480, 50),  7: (480, 50),  8: (480, 50),  9: (480, 50), 10: (480, 50),  
       11: (480, 50), 12: (480, 50), 13: (480, 50), 14: (480, 50), 15: (480, 50),  
       16: (480, 50), 17: (480, 50), 18: (480, 50), 19: (480, 50), 20: (480, 50),  
    },
    "Mon Amour": {    
        1: (480, 50),  2: (480, 50),  3: (480, 50),  4: (480, 50),  5: (480, 50),  
        6: (480, 50),  7: (480, 50),  8: (480, 50),  9: (480, 50), 10: (480, 50),  
       11: (480, 50), 12: (480, 50), 13: (480, 50), 14: (480, 50), 15: (480, 50),  
       16: (480, 50), 17: (480, 50), 18: (480, 50), 19: (480, 50), 20: (480, 50),  
    },
    "UKIJ": {    
        1: (500, 100),  2: (500, 100),  3: (500, 100),  4: (500, 100),  5: (500, 100),  
        6: (500, 100),  7: (500, 100),  8: (500, 100),  9: (500, 100), 10: (500, 100),  
       11: (500, 100), 12: (500, 100), 13: (500, 100), 14: (500, 100), 15: (500, 100),  
       16: (500, 100), 17: (500, 100), 18: (500, 100), 19: (500, 100), 20: (500, 100),  
    },
}

design_to_sku_to_second_fontsize_placement = {  
    "Al Libretto": (430, None, 690),  
    "Bella": (650, None, 690),  
    "Buffalo Nickel": (500, None, 690),  
    "Cervantiss": (620, None, 550),  
    "Claster Regular": (640, None, 550),  
    "Fairy-Bold": (500, None, 650),  
    "Nella Sue": (500, None, 650),  
    "Autumn Chant": (480, None, 650),  
    "Mon Amour": (480, None, 650),  
    "UKIJ": (500, None, 900),  
}

design_to_sku_to_third_fontsize_placement = {  
    "Al Libretto": (430, None, 1190),  
    "Bella": (650, None, 1290),  
    "Buffalo Nickel": (500, None, 1290),  
    "Cervantiss": (620, None, 1100),  
    "Claster Regular": (640, None, 1300),  
    "Fairy-Bold": (500, None, 1300),  
    "Nella Sue": (500, None, 1300),  
    "Autumn Chant": (480, None, 1300),  
    "Mon Amour": (480, None, 1300),  
    "UKIJ": (500, None, 1700),  
}

design_to_sku_to_fourth_fontsize_placement = {  
    "Al Libretto": (430, None, 1690),  
    "Bella": (650, None, 1890),  
    "Buffalo Nickel": (500, None, 1890),  
    "Cervantiss": (620, None, 1650),  
    "Claster Regular": (640, None, 2050),  
    "Fairy-Bold": (500, None, 1950),  
    "Nella Sue": (500, None, 1950),  
    "Autumn Chant": (480, None, 1950),  
    "Mon Amour": (480, None, 1950),  
    "UKIJ": (500, None, 2500),  
}