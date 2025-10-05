import sys
import csv

def main():
    #Menos de 1 argumento
    #if len(sys.argv) < 3:
         #sys.exit("Too few command-line arguments")
    #Mais de 1 argumento
    #elif len(sys.argv) > 3:
         #sys.exit("Too many command-line arguments")

    #Arquivo com o formato inválido
    input_file = sys.argv[1]
    #output_file = sys.argv[2]

    #if not input_file.endswith(".csv"):
        #sys.exit("Not a CSV file")


    def inverter(name, indicator):
        last_name, first_name = name.strip().split(indicator)
        return first_name.strip(), last_name.strip()

    dictFile = []

    try:
         with open(f"{sys.argv[1]}") as file:
             arquivo = csv.DictReader(file)
             columnName = arquivo.fieldnames
             columnName.append("house")
             #for _ in arquivo:
                     #_.update({"name": inverter(_.get("name"), ",")})
                     #dictFile.append(_)
             print(columnName)
    except FileNotFoundError:
         sys.exit(f"Could not read {sys.argv[1]}")

#main()

def inverter(name, indicator):
        last_name, first_name = name.strip().split(indicator)
        return first_name.strip(), last_name.strip()

dictFile = []

dictFile.append(inverter("Lovelace, Ada", ","))
dictFile.append(inverter("Hopper Grace", " "))
dictFile.append(inverter("Curie, Marie", ","))

print(dictFile)