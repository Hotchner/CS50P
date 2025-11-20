import csv

with open("carros.csv") as file:
    arquivo = csv.DictReader(file)
    print("BMW")
    for _ in arquivo:
        if _.get("Ano") < "2021":
            pass
        else:
            print(f'Modelo: {_.get("Modelo")} Ano: {_.get("Ano")}')
            # print(f"Modelo: {_.get('Modelo')}, Preço: {_.get('Preço')}")
            