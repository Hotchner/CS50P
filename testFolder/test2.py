def busca_binaria(x):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    mid_value = len(numbers) /2
    mid_value = int(mid_value)

    chute = numbers[mid_value] #Começa valendo 7

    while True:
        if chute == x:
            break

        elif x < mid_value:
            #Deletando do meio até o fim
            del numbers[mid_value:]
            mid_value = len(numbers) /2
            mid_value = int(mid_value)
            chute = numbers[mid_value]
            print(numbers)
            continue

        elif x > mid_value:
            #Deletando do inicio até o meio
            del numbers[:mid_value]
            mid_value = len(numbers) /2
            mid_value = int(mid_value)
            chute = numbers[mid_value]
            print(numbers)
            continue
    return chute

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
meio = len(numeros) /2
meio = int(meio)

#print("O número abaixo deve ser o 7")
#chute = numeros[meio]
#print(chute)

#print(meio)

print(busca_binaria(8))








#Deletando do meio até o fim
#del numbers[mid_value-1:]

#Deletando do inicio até o meio
#del numbers[:mid_value]
