import sys

linhasN = 0

def main():
    #Abrindo o arquivo em modo de leitura
    with open("exemplo.py", "r") as arquivo:
        #Lendo todas as linhas do arquivo e atribuindo elas a variável linhas
        linhas = arquivo.readlines()
        for _ in linhas:
            if _.startswith("#"):
                pass

            elif _.startswith(" ", 0, -1):
                pass

            else:
                linhasN += 1
        print(f"O texto possui {linhasN} linhas.")
