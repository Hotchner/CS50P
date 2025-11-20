# from PIL import Image, ImageOps

# imagem = Image.open("before1.jpg")

# tamanho = (600, 600)
# ajustada = ImageOps.fit(imagem, tamanho)

# ajustada.show();

# foto = Image.open("before1.jpg")
# camisa = Image.open("shirt.png").convert("RGBA")

# foto_ajustada = ImageOps.fit(foto, camisa.size) #Redimensiona a foto para o mesmo tamanho da camisa

# foto_ajustada.paste(camisa, (0, 0), camisa)

# foto_ajustada.show()


from PIL import Image

img = Image.open("before1.jpg")
img.show()
