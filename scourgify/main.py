from tabulate import tabulate
import sys
import csv

def main():
    #Menos de 1 argumento
    if len(sys.argv) < 3:
         sys.exit("Too few command-line arguments")
    #Mais de 1 argumento
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")

    #Arquivo com o formato inválido
    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

def main():
    beforeFile = []

    try:
        with open(f"{sys.argv[1]}") as file:
            arquivo = csv.DictReader(file)
            for _ in arquivo:
                beforeFile.append(_)
            print(tabulate(beforeFile, headers="keys", tablefmt='grid'))

            
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
main()