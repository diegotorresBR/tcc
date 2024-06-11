import matplotlib.pyplot as plt
from PIL import Image

def obter_nivel_cinza(imagem):
    img = Image.open(imagem)
    img_cinza = img.convert('L')
    largura, altura = img_cinza.size
    niveis_cinza = []
    for y in range(altura):
        for x in range(largura):
            nivel_cinza = img_cinza.getpixel((x, y))
            niveis_cinza.append(nivel_cinza)
    return niveis_cinza

def plotar_grafico(niveis_cinza):
    plt.hist(niveis_cinza, bins=256, color='gray', alpha=0.7)
    plt.xlabel('Nível de Cinza')
    plt.ylabel('Frequência')
    plt.title('Histograma de Níveis de Cinza')
    plt.show()

# Exemplo de uso
imagem = "raio.jpg"  # Substitua pelo caminho da sua imagem
niveis_cinza = obter_nivel_cinza(imagem)
plotar_grafico(niveis_cinza)