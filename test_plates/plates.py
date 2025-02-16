def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if plate_size(s) and two_letters(s) and acentuacao(s) and metade_placa(s):
        return True
    else:
        return False


#Verifica se o tamanho da placa está entre 2 e 6
def plate_size(x):
    size = len(x)
    return size in range(2, 7)

#Verifica se a placa começa com duas letras
def two_letters(x):
    return x[0:2].isalpha()

#Verifica se todos os caracteres da placa são alfa numéricos
def acentuacao(x):
    return x[0:-1].isalnum()

#Dividir a placa em duas partes para verificar
def metade_placa(x):
    #Numeros não podem ser usados no meio da placa
    #O Primeiro número do meio da placa não pode ser 0
    meio = len(x) / 2
    meio = int(meio)

    first_part = ""
    second_part = ""

    for _ in x:
        if len(first_part) < meio:
            first_part += _
        else:
            second_part += _

    if second_part[0] != "0" and second_part[0].isnumeric() and second_part.isnumeric():
        return True
    elif second_part[0].isalpha() and second_part[0:].isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
