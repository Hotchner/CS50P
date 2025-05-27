from tabulate import tabulate
import csv
import sys

# cabecalho = ["Sabor", "Preço"]
# pizza = []

# with open("pizzas.csv") as file:
#     leitor = csv.reader(file)
#     for _ in leitor:
#         pizza.append(_)

# print(tabulate(pizza, headers=cabecalho, tablefmt="fancy_grid"))


# cabecalho = ["Sabor", "Preço", "Pequeno"]
# pizza = []
# try:
#     with open("pizzas.csv") as file:
#         leitor = csv.reader(file)
#         for _ in leitor:
#             pizza.append(_)
#     print(tabulate(pizza, headers=cabecalho, tablefmt="fancy_grid"))
# except FileNotFoundError:
#     sys.exit("File does not exist")



with open("sicilian.csv") as file:
    pizzas = []
    arquivo = csv.DictReader(file)
    cabecalho = arquivo.fieldnames
    for _ in arquivo:
        pizzas.append(_)
    print(tabulate(pizzas, headers="keys", tablefmt="fancy_grid"))

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
        with open("sicilian.csv") as file:
            pizzas = []
            arquivo = csv.DictReader(file)
            for _ in arquivo:
                pizzas.append(_)
            print(tabulate(pizzas, headers="keys", tablefmt="fancy_grid"))
    except FileNotFoundError:
        sys.exit("File not exists")
main()