crop_details = {
    'rice': {
        'weather': {
            'im1': '/rice/rice1.jpg',
            'max_temp': 35,
            'min_temp': 25,
            'max_humidity': 80,
            'min_humidity': 84
        },
        'irrigation': {
            'max_water': 2500,
            'min_water': 900,
            'annual_rainfall': 100
        },
        'diseases': {
            'name': [ 'False smut', 'Bacterial blight','Bakanae', 'Blast (leaf and collar)'],
            'prevention': ['Use balanced amounts of plant nutrients, especially nitrogen.', 
            'Ensure good drainage of fields (in conventionally flooded crops) and nurseries.', 
            'Keep fields clean.', 
            'Allow fallow fields to dry in order to suppress disease agents in the soil and plant residues.'
            'Where possible, perform conservation tillage and continuous rice cropping.',
            'Use moderate rates of Nitrogen.'
            'Use certified seeds.'
            'Seed treatment with fungicide.']
        },
        'pests': {
            'Planthoppers': 'Imidacloprid',
            'Stem Borer	':  'Deltamethrin',
            'Aphid': 'Malathion',
            'Meal Bugs': 'Neem Oil',
            'Thrips': 'Spinosad',
            'Rice Bugs': 'Chlorpyriphos'
        },
        'fertilizers': {
            'N': 2,
            'P': 1,
            'K': 2,
            'ph_max': 7.2,
            'ph_min': 5.2,
            'fertilizer': {
                'UREA': 110,
                'DAP or SAP': 27,
                'MOP': 75,
                'ZINC': 20
            },
            'nutrient': {
                'nitrogen': 50,
                'phosphorous': 12,
                'potash': 50
            }
        },
    },
    'wheat': {
        'peas': {
            'im1': '//wheat1.jpg',
            'max_temp': 24,
            'min_temp': 21,
            'max_humidity': 80,
            'min_humidity': 60,
        },
        'irrigation': {
            'max_water': 600,
            'min_water': 450,
            'annual_rainfall': 100
        },
        'diseases': ['Bacterial leaf streak and black chaff', 'Basal glume rot', 'Barley yellow dwarf', 'Ergot disease', 'Powdery mildew', 'Phythium root rot'],
        'pests': {
            'planthoppers': 'Imidacloprid',
        },
        'fertilizers': {},
        'seed_details': {},
    },
    'wheat': {
        'weather': {
            'im1': '/wheat/wheat1.jpg',
            'max_temp': 24,
            'min_temp': 21,
            'max_humidity': 80,
            'min_humidity': 60,
        },
        'irrigation': {
            'max_water': 600,
            'min_water': 450,
            'annual_rainfall': 100
        },
        'diseases': ['Bacterial leaf streak and black chaff', 'Basal glume rot', 'Barley yellow dwarf', 'Ergot disease', 'Powdery mildew', 'Phythium root rot'],
        'pests': {
            'planthoppers': 'Imidacloprid',
        },
        'fertilizers': {},
        'seed_details': {},
    },'wheat': {
        'weather': {
            'im1': '/wheat/wheat1.jpg',
            'max_temp': 24,
            'min_temp': 21,
            'max_humidity': 80,
            'min_humidity': 60,
        },
        'irrigation': {
            'max_water': 600,
            'min_water': 450,
            'annual_rainfall': 100
        },
        'diseases': ['Bacterial leaf streak and black chaff', 'Basal glume rot', 'Barley yellow dwarf', 'Ergot disease', 'Powdery mildew', 'Phythium root rot'],
        'pests': {
            'planthoppers': 'Imidacloprid',
        },
        'fertilizers': {},
        'seed_details': {},
    },'wheat': {
        'weather': {
            'im1': '/wheat/wheat1.jpg',
            'max_temp': 24,
            'min_temp': 21,
            'max_humidity': 80,
            'min_humidity': 60,
        },
        'irrigation': {
            'max_water': 600,
            'min_water': 450,
            'annual_rainfall': 100
        },
        'diseases': ['Bacterial leaf streak and black chaff', 'Basal glume rot', 'Barley yellow dwarf', 'Ergot disease', 'Powdery mildew', 'Phythium root rot'],
        'pests': {
            'planthoppers': 'Imidacloprid',
        },
        'fertilizers': {},
        'seed_details': {},
    },'wheat': {
        'weather': {
            'im1': '/wheat/wheat1.jpg',
            'max_temp': 24,
            'min_temp': 21,
            'max_humidity': 80,
            'min_humidity': 60,
        },
        'irrigation': {
            'max_water': 600,
            'min_water': 450,
            'annual_rainfall': 100
        },
        'diseases': ['Bacterial leaf streak and black chaff', 'Basal glume rot', 'Barley yellow dwarf', 'Ergot disease', 'Powdery mildew', 'Phythium root rot'],
        'pests': {
            'planthoppers': 'Imidacloprid',
        },
        'fertilizers': {},
        'seed_details': {},
    },
}

def get_data(crop, data_name):
    if crop in crop_details:
        return crop_details[crop][data_name]
    return None