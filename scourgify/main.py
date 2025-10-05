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
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        sys.exit("Not a CSV file")


    def inverter(name, indicator):
        last_name, first_name = name.strip().split(indicator)
        return first_name.strip(), last_name.strip()

    dictFile = []

    try:
         with open(f"{sys.argv[1]}") as file: #Abrindo o arquivo e colocando uma variável nele
             arquivo = csv.DictReader(file) #Lendo o arquivo como dicionário
             for _ in arquivo: #Percorrendo o arquivo
                     first, last = inverter(_.get("name"), ",")
                     _.update({"first_name": first, "last_name": last})
                     del _["name"]  # remove a chave antiga
                     dictFile.append(_) #Adicionando o dicionário na lista
         
         with open(f"{sys.argv[2]}", "w", newline="") as file:
              arquivo = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
              arquivo.writeheader()
              arquivo.writerows(dictFile)
    except FileNotFoundError:
         sys.exit(f"Could not read {sys.argv[1]}") 
    
main()