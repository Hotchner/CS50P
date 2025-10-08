from PIL import Image, ImageOps
import sys


def main():
    #Menos de 1 argumento
    if len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    #Mais de 1 argumento
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")

    foto = Image.open(sys.argv[1]).convert("RGBA")
    overlay = Image.open(sys.argv[2]).convert("RGBA")

    foto_ajustada = ImageOps.fit(foto, overlay.size)

    foto_ajustada.paste(overlay, (0, 0), overlay)

    foto_ajustada.show()

main()
