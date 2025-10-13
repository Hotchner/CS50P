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
          
     file_name_1, file_type_1 = os.path.splitext(sys.argv[1])
     file_name_2, file_type_2 = os.path.splitext(sys.argv[2])

     if file_type_1 != file_type_2:
          sys.exit("Input and output have different extensions")
     elif file_type_2 not in formatos_aceitos:
          sys.exit("Invalid output")
     elif os.path.exists(f"{file_name_1}") == False:
          sys.exit("Input does not exist")
     else:
          print("Pass")
     

main()