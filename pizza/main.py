from tabulate import tabulate
import sys
import csv

def main():
    #Menos de 1 argumento
    if len(sys.argv) < 2:
         sys.exit("Too few command-line arguments")
    #Mais de 1 argumento
    elif len(sys.argv) > 2:
         sys.exit("Too many command-line arguments")

    #Arquivo com o formato inválido
    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(f"{sys.argv[1]}") as file:
            pizzas = []
            arquivo = csv.DictReader(file)
            for _ in arquivo:
                pizzas.append(_)
            print(tabulate(pizzas, headers="keys", tablefmt="fancy_grid"))
    except FileNotFoundError:
        sys.exit("File not exists")
main()