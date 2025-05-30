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

    beforeFile = []

    def inverter(name, indicator, column):
        name_old = name.get(f"{column}")
        last_name, first_name = name_old.split(f"{indicator}")
        new_name = f"{first_name}, {last_name}".strip()
        return new_name

    try:
        with open(f"{sys.argv[1]}") as file:
            arquivo = csv.DictReader(file)
            for _ in arquivo:
                name_old = _.get("name")
                l_name, f_name = name_old.split(",")
                new_name = f"{f_name}, {l_name}".strip()
                beforeFile.append(new_name)

                
            print(beforeFile)

            
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
main()