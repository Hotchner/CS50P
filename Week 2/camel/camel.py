def main():

    palavra = input("camelCase: ")

    newPalavra = ""

    for letra in palavra:
        if letterUper(letra):
            newPalavra += "_"
            letra = letra.lower()
            newPalavra += letra
        else:
            newPalavra += letra
    return print(f"snake_case: {newPalavra}")


def letterUper(x):
    return x.isupper()

main()
