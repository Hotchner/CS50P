from PIL import Image, ImageOps
import sys
import os


def main():
     #Menos de 1 argumento
     if len(sys.argv) < 3:
          sys.exit("Too few command-line arguments")
     #Mais de 2 argumento
     elif len(sys.argv) > 3:
          sys.exit("Too many command-line arguments")

     formatos_aceitos = [".jpg", ".jpeg", ".png"]

     input_name, input_type = os.path.splitext(sys.argv[1])
     output_name, output_type = os.path.splitext(sys.argv[2])

     if output_type not in formatos_aceitos:
          sys.exit("Invalid output")
     elif input_type != output_type:
          sys.exit("Input and output have different extensions")
     elif os.path.exists(sys.argv[1]) == False:
          sys.exit("Input does not exist") 
     else:
          pass

     photo = Image.open(sys.argv[1])
     cs50_shirt = Image.open("shirt.png").convert("RGBA") #PNG da camisa

     photo2 = ImageOps.fit(photo, cs50_shirt.size)
     photo2.paste(cs50_shirt, (0, 0), cs50_shirt)

     photo2.save(f"{output_name}{output_type}")
     photo2.show()

main()