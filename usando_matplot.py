import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def plot_intensity(image_path):
    # Carrega a imagem
    img = mpimg.imread(image_path)

    # Obtém as dimensões da imagem
    height, width, _ = img.shape

    # Converte a imagem para escala de cinza (média dos canais de cor)
    gray_img = np.mean(img, axis=2)

    # Cria um vetor de posições de pixel
    pixel_positions = np.arange(width)

    # Calcula a média da intensidade de cor ao longo do eixo vertical
    intensity_values = np.mean(gray_img, axis=0)

    # Plota a intensidade da cor como uma função linear
    plt.plot(pixel_positions, intensity_values, color='b', label='Intensidade de cor')
    plt.title('Intensidade de Cor ao Longo da Largura da Imagem')
    plt.xlabel('Posição do Pixel na Largura')
    plt.ylabel('Intensidade de Cor (Escala de Cinza)')
    plt.legend()
    plt.show()

# Caminho para a sua imagem
caminho_da_imagem = "raio.jpg"

# Chama a função para plotar a intensidade
plot_intensity(caminho_da_imagem)
