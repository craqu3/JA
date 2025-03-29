
"""
    Programador....: (C) 2025 . Ricardo Pires
    Data...........: 26/03/2025
    Observações....: Carregar o modelo treinado e testar imagens com classificação.
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image


# Definir as 10 classes do CIFAR-10
labels = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# Permite carregar o modelo
model = load_model('cnn_model.h5')

# Função para carregar e processar a imagem de teste
def process_image(img_path):
    img = image.load_img(img_path, target_size=(32, 32))  # Redimensionar a imagem para 32x32
    img_array = image.img_to_array(img)  # Converter para array numpy
    img_array = np.expand_dims(img_array, axis=0)  # Adicionar a dimensão do batch (1 imagem)
    img_array = img_array / 255.0  # Normalizar os valores dos pixels para o intervalo [0,1]
    return img_array

# Função para fazer a previsão
def predict_image(img_path):
    img_array = process_image(img_path)
    prediction = model.predict(img_array)  # Realiza a previsão
    predicted_class = np.argmax(prediction)  # Obter a classe com maior probabilidade
    return predicted_class, prediction

img_path = 'images/cifar-10/test/193.png'
predicted_class, prediction = predict_image(img_path)

img = image.load_img(img_path, target_size=(32, 32))
plt.imshow(img)
plt.title(f'Predicted: {labels[predicted_class]}')
plt.show()

print(f'Predicted class: {labels[predicted_class]}')
print(f'Prediction probabilities: {prediction}')