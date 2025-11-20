def remove_letter(): #Criando a função remove_letter()

    wovels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"] #Criando uma lista com todas as vogais

    word = input("Input: ") #Solicitando a frase
    new_word = "" #Variável vazia

    for letter in word: #Para cada letra da palavra informada:
        if letter in wovels: #Se a letra atual estiver na lista de vogais (wovels[])
            letter.replace(letter, "") #Substitua/remova essa letra e vá para a próxima
        else: #Caso essa letra não esteja na lista de vogais:
            new_word = new_word + letter #Adicione ela na variável (new_word)
    return print(new_word) #Ao final do loop for, retorne a variável new_word completa

remove_letter() #Chamando a função
