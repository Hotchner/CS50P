from PIL import Image, ImageDraw

# Cria uma imagem 600x600 transparente
img = Image.new("RGBA", (600, 600), (0, 0, 0, 0))

# Cria um círculo vermelho com transparência parcial
draw = ImageDraw.Draw(img)
draw.ellipse((100, 100, 500, 500), fill=(255, 0, 0, 180))  # 180 = transparência

# Salva a imagem
img.save("circulo_transparente.png")
print("Imagem criada: circulo_transparente.png")

