from PIL import Image

#imagem_original = Image.open("imagem_desgaste.jpg")
#pixels = imagem_original.load()
#tam_vizi = (2,4)
#vizinhos = []
#larg, altu = imagem_original.size

def vizinhanca(imagem = Image.open("imagem_desgaste.jpg"), tam_vizi=(2,2)):
    imagem.show()
    pixels = imagem.load()
    vizinhos = []
    larg, altu = imagem.sizez

    for x in range(larg):
        for y in range(altu):
            #obtendo os vizinhos
            try:
                for i in range(tam_vizi[0]):
                    for j in range(tam_vizi[1]):
                        # pixels[x,y] = ()
                        vizinhos.append(pixels[x+1 + i, y])
                        vizinhos.append(pixels[x - 1 - i , y])
                        vizinhos.append(pixels[x, y + 1 + j])
                        vizinhos.append(pixels[x, y - 1 - j])
                        vizinhos.append(pixels[x + 1 + i, y + 1 + j])
                        vizinhos.append(pixels[x + 1 + i, y - 1 - j])
                        vizinhos.append(pixels[x - 1 - i, y + 1 + j])
                        vizinhos.append(pixels[x - 1 - i, y - 1 - j])
            except:
                print("bordas")
            pixels[x,y] = operacao(vizinhos)
            vizinhos.clear()
    img_viz = imagem
    img_viz.show()

def operacao(pixel):
    #media
    r,g,b = (0,0,0)
    # r,g,b = (r/len(pixel)), (g/len(pixel)), (b/len(pixel)) if len(pixel)>0 else (0,0,0)
    if(len(pixel) > 0):
        for x in pixel:
            r1, g1, b1 = x
            r += r1
            g += g1
            b += b1
        r = r // len(pixel)
        g = g // len(pixel)
        b = b // len(pixel)

    return r,g,b


imagem = Image.open("imagem_desgaste.jpg")
vizinhanca(imagem)
# if __name__ == '__main__':
#     #imagem_original.show()
#     imagem = Image.open("imagem_desgaste.jpg")
#     vizinhanca(imagem)