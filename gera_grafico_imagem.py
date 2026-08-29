import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def gera_grafico_imagem(caminho_imagem, tamanho_maximo=(200, 200), salvar_como=None, cmap="gray"):
    """
    Gera o gráfico 3D da superfície de uma imagem dada pela função g(f) = (x, y, z),
    onde (x, y) são as coordenadas do plano cartesiano e z = f(x, y) representa
    a intensidade de brilho (ou tom de cinza) do pixel na posição (x, y).

    Parâmetros:
    -----------
    caminho_imagem : str
        Caminho para o arquivo de imagem de entrada.
    tamanho_maximo : tuple (largura, altura)
        Redimensiona a imagem para evitar lentidão na renderização 3D.
    salvar_como : str (opcional)
        Caminho para salvar a figura gerada (ex: 'grafico_superficie.png').
    cmap : str
        Mapa de cores para a superfície (ex: 'viridis', 'gray', 'plasma', 'jet').
    """
    # 1. Carrega a imagem e converte para escala de cinza
    imagem = Image.open(caminho_imagem).convert("L")

    # Redimensiona a imagem mantendo a proporção para otimizar o plot 3D
    if tamanho_maximo:
        imagem.thumbnail(tamanho_maximo)

    # 2. Obtém a matriz de intensidade f(x, y) normalizada no intervalo [0.0, 1.0]
    # Z representa f(x, y) onde 0.0 = preto puro e 1.0 = branco puro
    Z = np.array(imagem, dtype=float) / 255.0
    altura, largura = Z.shape

    # 3. Cria a grade cartesiana (X, Y)
    x = np.arange(0, largura)
    y = np.arange(0, altura)
    X, Y = np.meshgrid(x, y)

    # 4. Configura o gráfico 3D g(f) = (x, y, z)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plota a superfície z = f(x, y)
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, antialiased=True)

    # Limita o eixo Z no intervalo [0, 1]
    ax.set_zlim(0.0, 1.0)

    # Ajusta os rótulos dos eixos
    ax.set_title("Gráfico 3D da Imagem: g(f) = (x, y, z) onde z = f(x, y) ∈ [0, 1]", fontsize=14)
    ax.set_xlabel("Eixo X (Largura)", fontsize=11)
    ax.set_ylabel("Eixo Y (Altura)", fontsize=11)
    ax.set_zlabel("Eixo Z - Intensidade f(x, y)", fontsize=11)

    # Adiciona a barra de cores (colorbar)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="Intensidade f(x, y) [0.0 (Preto) - 1.0 (Branco)]")

    # Inverte o eixo Y para corresponder às coordenadas de imagem padrão (origem no topo esquerdo)
    ax.invert_yaxis()

    # Salva o gráfico caso um caminho de saída seja especificado
    if salvar_como:
        plt.savefig(salvar_como, dpi=300, bbox_inches="tight")
        print(f"Gráfico 3D salvo em: {salvar_como}")

    # Exibe o gráfico se houver interface gráfica disponível
    if plt.get_backend().lower() != 'agg':
        plt.show()

if __name__ == "__main__":
    caminho = "arara_cinza.jpg"
    gera_grafico_imagem(caminho, tamanho_maximo=(150, 150), salvar_como="grafico_imagem_3d.png")

