
from random import randint
import tensorflow as tf


model = tf.keras.models.load_model('/workspace/demologin/project/new_nn.h5')

soil = ["",
        "clay loam",  # 1
        "loamy soil",  # 2
        "sandy loam",  # 3
        "black soil",  # 4
        "alluvial soil",  # 5
        "laterite soil",  # 6
        "red soil",  # 7
        "silty loam",  # 8
        "neurtral soil"]  # 9

croplist = [{'name': 'Paddy', 'growth_period': '180 - 195 days', 'soil_type': 'clay soil', 'water': '.1000'}, {'name': 'Wheat', 'growth_period': '7-8 months', 'soil_type': 'clay loam,loamy soil', 'water': '.500'}, {'name': 'Onion', 'growth_period': '5 months', 'soil_type': 'sandy loam', 'water': '.500'}, {'name': 'Potato', 'growth_period': '70-120 days', 'soil_type': 'loamy soil', 'water': '.500'}, {'name': 'Safflower', 'growth_period': '120days', 'soil_type': 'alluvial soil,black soil', 'water': '.375'}, {'name': 'Cotton', 'growth_period': '115-125 days', 'soil_type': 'black soil,sandy loam,', 'water': '.500'}, {'name': 'Orange', 'growth_period': '10 - 15 yrs', 'soil_type': 'sandy loam', 'water': '.750'}, {'name': 'Banana', 'growth_period': '300 - 365 days', 'soil_type': 'loamy soil', 'water': '.875'}, {'name': 'Grapes', 'growth_period': '3 yrs', 'soil_type': 'loamy soil', 'water': '.1000'}, {'name': 'Tomato', 'growth_period': '60-70 days', 'soil_type': 'loamy soil', 'water': '.500'}, {'name': 'Pomegranate', 'growth_period': '4-5yrs', 'soil_type': 'loamy soil', 'water': '.625'}, {'name': 'Sorgham', 'growth_period': '100-115 days', 'soil_type': 'clay loam', 'water': '.625'}, {'name': 'Sugarcane', 'growth_period': '12-18months', 'soil_type': 'loamy soil', 'water': '.1000'}, {'name': 'Chilli', 'growth_period': '60-120days', 'soil_type': 'loamy soil', 'water': '.1000'}, {'name': 'Mungbean', 'growth_period': '90days-120days', 'soil_type': 'sandy loam', 'water': '.500'}, {'name': 'Groundnut', 'growth_period': '85-200 days', 'soil_type': 'loamy soil,sandy loan,', 'water': '.1000'}, {'name': 'Millets', 'growth_period': '60-70 days', 'soil_type': 'loamy soil', 'water': '.375'}, {'name': 'Peas', 'growth_period': '70 days', 'soil_type': 'sandy loam', 'water': '.375'}, {'name': 'Tea', 'growth_period': '2 years', 'soil_type': ['sandy loam', 'silty loam'], 'water': '.375'}, {'name': 'Coffee', 'growth_period': '7-9 months', 'soil_type': 'sandy loam', 'water': '.1000'}, {'name': 'Mango', 'growth_period': '5-6 months', 'soil_type': 'sandy loam', 'water': '.875'}, {'name': 'Coconut', 'growth_period': '15-20 years', 'soil_type': 'laterite soil,sandy loam,alluvial,red soil', 'water': '.250'}, {'name': 'Jute', 'growth_period': '120-180days', 'soil_type': 'loamy soil', 'water': '.875'}, {'name': 'Rubber', 'growth_period': '90-180days ', 'soil_type': 'loamy soil', 'water': '.1000'}, {'name': 'Blackgram', 'growth_period': '', 'soil_type': 'loamy soil', 'water': '.1000'}, {'name': 'Watermelon', 'growth_period': '', 'soil_type': 'sandy loam', 'water': '.125'}, {'name': 'Apple', 'growth_period': '', 'soil_type': 'loamy soil', 'water': '.125'}, {'name': 'Maize', 'growth_period': '', 'soil_type': 'alluvial soil', 'water': '.1000'}, {'name': 'Lentil', 'growth_period': '', 'soil_type': 'sandy loam', 'water': '.1000'}, {'name': 'Tobacco', 'growth_period': '100-120 days', 'soil_type': 'black soil,alluvial,loamy soil,loamy soil', 'water': '.625'}, {'name': 'Kidney beans', 'growth_period': '50-67 days', 'soil_type': 'sandy loam,clay loam,loamy,', 'water': '.625'}, {'name': 'Mouth beans', 'url': 'static/beans.png', 'growth_period': '55 days ', 'soil_type': 'sandy loam,silty loam', 'water': '.125'}, {'name': 'Adzuki beans', 'url': 'static/beans.png', 'growth_period': '50-55 days', 'soil_type': 'neutral soil,alkaline,', 'water': '.500'}, {'name': 'Pigeon beans', 'url': 'static/bean.png', 'growth_period': '120 to 180 days', 'soil_type': 'sandy loam,loamy soil', 'water': '.500'}, {'name': 'Chick peas', 'growth_period': '40 to 80 days', 'soil_type': 'black soil ,heavy soil', 'water': '.125'}, {'name': 'Muskmelon', 'growth_period': '90 days ', 'soil_type': 'sandy loam,sandy soil', 'water': '.125'}]


def get_noutput(n_output, temp, hum, ph, rain, water):
    noutput = []
    nlabel = []
    output1 = get_output(temp, hum, ph, rain, water)[0]
    noutput.append(output1)
    label1 = get_label(output1)
    nlabel.append(label1)
    count = 1
    while count < n_output:
        new_output = get_output(temp+randint(-5,5), hum+randint(-20,20), ph+randint(-1,1), rain+randint(-20, 20), water)[0]
        new_label = get_label(new_output)
        if new_label not in nlabel:
            count += 1
            noutput.append(new_output)
            nlabel.append(new_label)
    count = 0
    ndict = {}
    for name in nlabel:
        for crop in croplist:
            cname = crop.get('name', None)
            if cname.lower() == name.lower():
                count += 1
                ndict['crop'+str(count)] = crop

    return ndict


def get_output(temp, hum, ph, rain, water):
    return model.predict([[temp, hum, ph, rain, water]])


def get_label(output):
    output = list(output)
    crops = ['rice', 'wheat', 'Mung Bean', 'Tea', 'millet', 'maize', 'Lentil', 'Jute', 'Coffee', 'Cotton', 'Ground Nut', 'Peas', 'Rubber', 'Sugarcane', 'Tobacco', 'Kidney Beans', 'Moth Beans', 'Coconut', 'Black gram', 'Adzuki Beans', 'Pigeon Peas', 'Chickpea', 'banana', 'grapes', 'apple', 'mango', 'muskmelon', 'orange', 'papaya', 'pomegranate', 'watermelon']
    val = output.index(max(output))
    return crops[val]
