from PIL import Image

imagem_p_e_b = Image.open("imagem_para_inverter.jpeg")
pixels = imagem_p_e_b.load()

print(imagem_p_e_b.size)
print(pixels[639, 359])
def vizinhanca():
    pass
