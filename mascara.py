from PIL import Image

imagem_original = Image.open("imagem_desgaste.jpg")
pixels = imagem_original.load()
tam_vizi = (4,4)

larg, altu = imagem_original.size

def vizinhanca():

    for x in range(larg):
        for y in range(altu):
            #obtendo os vizinhos
            for i in range(tam_vizi[0]):
                for j in range(tam_vizi[1]):
                    # pixels[x,y] = ()
                    print(i, j)

            # r,g,b = pixels[x,y]


def operacao(pixel):
    pass

vizinhanca()