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