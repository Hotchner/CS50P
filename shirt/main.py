from PIL import Image, ImageOps
import sys
import os


def main():
     # #Menos de 1 argumento
     # if len(sys.argv) < 3:
     #      sys.exit("Too few command-line arguments")
     # #Mais de 2 argumento
     # elif len(sys.argv) > 3:
     #      sys.exit("Too many command-line arguments")
     
     formatos_aceitos = [".jpg", ".jpeg", ".png"]
          
     # input_name_1, output_type_1 = os.path.splitext(sys.argv[1])
     # file_name_2, file_type_2 = os.path.splitext(sys.argv[2])

     #photo_1 = Image.open(sys.argv[1]).convert("RGBA")

     photo = Image.open(sys.argv[1])
     cs50_shirt = Image.open("shirt.png").convert("RGBA") #PNG da camisa

     photo2 = ImageOps.fit(photo, cs50_shirt.size)
     photo2.paste(cs50_shirt, (0, 0), cs50_shirt)

     photo2.show()
     # if file_type_1 != file_type_2:
     #      sys.exit("Input and output have different extensions")
     # elif 


main()