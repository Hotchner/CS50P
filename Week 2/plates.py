def metade_da_palavra(x):
    qtd_letras = len(x)

    metade_letras = qtd_letras /2

    primeira_parte = ""
    segunda_parte = ""

    for letra in x:
        if len(primeira_parte) < metade_letras:
            primeira_parte = primeira_parte + letra
        else:
            segunda_parte = segunda_parte + letra
    return primeira_parte, segunda_parte, x

def duas_primeiras_letras(x):
    return x[0:2].isalpha()

def placaSize(x):
    return len(x) >= 2 and len(x) <= 6 

def is_valid(x):

    primeira_parte, segunda_parte, palavraFinal = metade_da_palavra(x)

    if duas_primeiras_letras(primeira_parte) and placaSize(palavraFinal) and segunda_parte[0] != "0" and palavraFinal.isalnum():
        return True
    
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()