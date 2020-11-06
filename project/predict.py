import tensorflow as tf
from random import randint

model = tf.keras.models.load_model('new_nn.h5')


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
    return nlabel


def get_output(temp, hum, ph, rain, water):
    return model.predict([[temp, hum, ph, rain, water]])


def get_label(output):
    output = list(output)
    crops = ['rice', 'wheat', 'Mung Bean', 'Tea', 'millet', 'maize', 'Lentil', 'Jute', 'Coffee', 'Cotton', 'Ground Nut', 'Peas', 'Rubber', 'Sugarcane', 'Tobacco', 'Kidney Beans', 'Moth Beans', 'Coconut', 'Black gram', 'Adzuki Beans', 'Pigeon Peas', 'Chickpea', 'banana', 'grapes', 'apple', 'mango', 'muskmelon', 'orange', 'papaya', 'pomegranate', 'watermelon']
    val = output.index(max(output))
    return crops[val]
