import csv

#Dados em dicionário
dados = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Bianca", "idade": 28}
]

#Iniciando o método With
with open("saida.csv", "w", newline="") as arquivo: #Vai ser criado um arquivo "saida.csv", será aberto no modo escritura
    campos = ["nome", "idade"] #Cabeçalhos 
    escritor = csv.DictWriter(arquivo, fieldnames=campos) #Escrevendo os cabeçalhos no arquivo 
    escritor.writeheader()#Preciso entender essa função
    escritor.writerows(dados)#Escrevendo 
