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
            del numbers[chute-1:]
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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mid_value = len(numbers) /2
mid_value = int(mid_value)


print(mid_value)
