from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
# Listando todas as fontes
# print(figlet.getFonts())
# Pegando uma fonte aleatória
# figlet.setFont(font=random.choice(figlet.getFonts()))
figlet.setFont(font="slant")
art_text = figlet.renderText("Hello, World")
# print(art_text)


def main():
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
        text = input("Input: ")
        text_custom = figlet.renderText(f"{text}")
        print(text_custom)
    
    elif len(sys.argv) == 3 and is_valid(sys.argv[2]) and sys.argv[1] == "--font" or sys.argv[1] == "-f":
        figlet.setFont(font=f"{sys.argv[2]}")
        text = input("Input: ")
        text_custom = figlet.renderText(f"{text}")
        print(text_custom)
    
    else:
        sys.exit("Invalid usage")



# Função para verificar se a fonte escolhida está no catálogo
def is_valid(x):
    return x in figlet.getFonts()

main()
