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

    def inverter(name, indicator):
        name_old = name.strip().replace(" ", "")
        last_name, first_name = name_old.split(f"{indicator}")
        new_name = f"{first_name}, {last_name}"
        return new_name

    beforeFile = []

    try:
        with open(f"{sys.argv[1]}") as file:
            arquivo = csv.DictReader(file)
            for _ in arquivo:
                    _.update({"name": inverter(_.get("name"), ",")})
                    beforeFile.append(_)     
        with open()

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}") 
main()