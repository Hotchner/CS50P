from PIL import Image, ImageOps
import sys
import os


def main():
    #Menos de 1 argumento
    if len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    #Mais de 1 argumento
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")
    
    formatos_aceitos = []
         

    foto1_nome, foto1_formato = os.path.splitext(sys.argv[1])
    foto2_nome, foto2_formato = os.path.splitext(sys.argv[2])

    print(foto1_formato, foto2_formato)

main()
