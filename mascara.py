from PIL import Image

imagem_original = Image.open("imagem_desgaste.jpg")
pixels = imagem_original.load()
tam_vizi = (1,1)
vizinhos = []
larg, altu = imagem_original.size

def vizinhanca():

    for x in range(larg):
        for y in range(altu):
            #obtendo os vizinhos
            try:
                for i in range(tam_vizi[0]):
                    for j in range(tam_vizi[1]):
                        # pixels[x,y] = ()
                        vizinhos.append(pixels[x+j+1, y+j])
                        vizinhos.append(pixels[x + i + 2, y + j + 1])
                        vizinhos.append(pixels[x + i + -1, y + j + 1])
                        vizinhos.append(pixels[x + i + 1, y + j + 1])
                        vizinhos.append(pixels[x + i + 1, y + j + 1])
                        vizinhos.append(pixels[x + i + 1, y + j + 1])
                        vizinhos.append(pixels[x + i + 1, y + j + 1])
                        vizinhos.append(pixels[x + i + 1, y + j + 1])

                    print(pixels[x,y], "Vizinho:", pixels[x+i+1, y+j+1])
            except:
                pass

                    # print(vizinhos)
            # print(len(vizinhos))
            vizinhos.clear()

            # r,g,b = pixels[x,y]


def operacao(pixel):
    pass

vizinhanca()