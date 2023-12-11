mv = 0

if not mv:
    print("Accepted")
else:
    print("Denied")

a = dict(one=1, two=2, three=3)
# print(a)
b = {'one': 1, 'two': 2, 'three': 3}
# print(b)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# print(c)

#removendo um item do dicionário
del a["one"]
print(a)

#Verificando se um item está no dicionário
print("one" in a)

#Verificando se um item não está em um dicionário
print("one" not in a)

#Limpando todos os items de um dicionário
b.clear()
print(b)

#Armazenando em uma variável a cópia de uma lista
c_Backup = c.copy()
print(c_Backup)

#Apagando todos os items da lista que eu fiz a cópia
c.clear()
print(c)

#Verificando a cópia da lista que foi formatada
print(c_Backup)

#Pegando todos os valores de um dicionáio
print(list(c_Backup.values()))

print("-" *50)

dishes = {'eggs': 3, 'sausage': 2, 'bacon': 1, 'spam': 500}

#Pegando somente as chaves do diconário
keys = dishes.keys()

#Pegando somente os valores do dicionário
values = dishes.values()

print("Valores:")
print(keys)
print("Chaves:")
print(values)

n = 0

for value in values:
    n += value

print(n)

#Deletando items
del dishes['sausage']
del dishes['spam']

print(keys)

print(dishes)

dishes['eggs'] = 6

print(dishes) 

dishes.update({'bananas': 5})

print(dishes.keys())



