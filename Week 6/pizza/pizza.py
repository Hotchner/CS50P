import sys
import csv
import tabulate

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
        pizza = []
        with open(f"{sys.argv[1]}") as file:
            leitor = csv.reader(file)
            for _ in leitor:
                pizza.append(_)
        print(tabulate(pizza, headers=headers, tablefmt="fancy_grid"))
    except FileNotFoundError:
        sys.exit("File not exists")
main()