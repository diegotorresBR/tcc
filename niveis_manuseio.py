from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import vizinhos

img = Image.open("gauss.jpeg")
def filtragem_espacial():
    #Precisa dessa função para definir qual a operação para gerar a imagem de saída
    #soma para redução de ruídos

    vizinhos.vizinhanca(img)

    pass
def obter_valores_pixel_pb(caminho_imagem):
    # Abre a imagem
    imagem = Image.open(caminho_imagem)

    # Converte a imagem para o modo L (escala de cinza)
    imagem = imagem.convert('L')

    # Obtém os valores dos pixels
    pixels = list(imagem.getdata())

    # Converte a lista de pixels em uma matriz bidimensional (linhas x colunas)
    largura, altura = imagem.size
    matriz_pixels = [pixels[i * largura:(i + 1) * largura] for i in range(altura)]

    return matriz_pixels


def plotar_valores_pb(matriz_pixels):
    # Converte a matriz de pixels em um array numpy
    matriz_pixels = np.array(matriz_pixels)

    # Achata o array bidimensional em unidimensional
    pixels = matriz_pixels.flatten()

    # Cria um array de índices para os pixels
    indices = np.arange(len(pixels))

    # Plota os valores em escala de cinza
    plt.figure(figsize=(10, 6))
    plt.plot(indices, pixels, 'k.', label='Gray', markersize=1)

    plt.xlabel('Pixel Index')
    plt.ylabel('Intensity')
    plt.title('Grayscale Values of Image Pixels')
    plt.legend()
    plt.show()


# Exemplo de uso
matriz_pixels = obter_valores_pixel_pb('gauss.jpeg')
#plotar_valores_pb(matriz_pixels)
filtragem_espacial()