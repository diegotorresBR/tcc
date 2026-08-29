from PIL import Image

def converter_escala_cinza(caminho_entrada, caminho_saida):
    """
    Converte uma imagem para escala de cinza (tons de cinza).
    """
    imagem = Image.open(caminho_entrada)
    # O modo 'L' converte a imagem para escala de cinza (8-bit pixels, 0 a 255)
    imagem_cinza = imagem.convert("L")
    imagem_cinza.save(caminho_saida)
    print(f"Imagem em escala de cinza salva em: {caminho_saida}")

def converter_preto_e_branco_puro(caminho_entrada, caminho_saida, limiar=128):
    """
    Converte uma imagem para preto e branco puro (binária: apenas pixels pretos e brancos),
    utilizando um limiar (threshold).
    
    Pixels com valor de cinza abaixo do limiar viram 0 (preto).
    Pixels com valor igual ou acima do limiar viram 255 (branco).
    """
    imagem = Image.open(caminho_entrada).convert("L")
    # Aplica o limiar (thresholding)
    imagem_pb = imagem.point(lambda p: 255 if p >= limiar else 0, mode="1")
    imagem_pb.save(caminho_saida)
    print(f"Imagem em preto e branco (binária) salva em: {caminho_saida}")

if __name__ == "__main__":
    caminho_imagem = "arara.png"
    
    # 1. Converter para escala de cinza
    converter_escala_cinza(caminho_imagem, "imagem_cinza.jpg")
    
    # 2. Converter para preto e branco puro (binário)
    converter_preto_e_branco_puro(caminho_imagem, "imagem_pb.jpg", limiar=128)
