import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image


def plot_intensity(image_path):
    # Carrega a imagem
    imag = Image.open(image_path)
    img = imag.convert("RGB")
    # img.show()
    # pixels = img.load()

    # Obtém as dimensões da imagem
    # height, width, _ = img.shape
    larg, altu = img.size

    # Cria um vetor de posições de pixel
    # pixel_positions = np.arange(width)

    list_val = []

    for x in range(larg):
        for y in range(altu):
            list_val.append(pixels[x, y])

    min_valor = min(list_val)
    max_valor = max(list_val)


    # Plota a intensidade como uma função linear
    plt.plot(, list_val,color='b', label='Intensidade de cor')
    plt.title('Intensidade ao Longo da Largura da Imagem')
    plt.xlabel('Posição do Pixel na Largura')
    plt.ylabel('Intensidade de Cor (Escala de Cinza)')
    plt.legend()
    plt.show()

# Caminho para a sua imagem
caminho_da_imagem = "gauss.jpeg"

# Chama a função para plotar a intensidade
plot_intensity(caminho_da_imagem)
