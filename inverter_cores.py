from PIL import Image


imagem_original = Image.open("imagem_para_inverter.jpeg")

pixels = imagem_original.load()
largura, altura = imagem_original.size
# Inverter as cores
#imagem_invertida = Image.eval(imagem_original, lambda x: 255 - x)
for i in range(largura):
        for j in range(altura):
            # Obtém o valor RGB do pixel
            r, g, b = pixels[i, j]

            # Inverte as cores subtraindo cada componente RGB de 255
            r = 255 - r
            g = 255 - g
            b = 255 - b

            # Define a nova cor no pixel
            pixels[i, j] = (r, g, b)
# Salvar a imagem invertida
imagem_invertida = pixels.image
imagem_invertida.save("imagem_invertida.jpg")


