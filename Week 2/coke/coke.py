def main(): #Criando a função main()

    saldo_a_pagar = 50 #Definindo um saldo a pagar
    coins_accepted = [5, 10, 25] #Lista de moedas que são aceitas

    while saldo_a_pagar > 0: #Enquanto o saldo a pagar for maior que 0

        print(f"Amount Due: {saldo_a_pagar}") #Inicie o loop informando o saldo atual
        coin_insert = int(input("Insert Coin: ")) #E logo em seguida solicite a entrada do usuário

        if coin_insert not in coins_accepted: #Se a entrada informada pelo usuário não estiver na lista de moedas aceitas
            continue #Reinicie o loop

        elif coin_insert in coins_accepted: #Mas caso a entrada informada pelo usuário (coin) esteja na lista de moedas aceitas (coins_acepted)
            saldo_a_pagar = saldo_a_pagar - coin_insert #Será debitado da variável saldo a pagar, o valor inserido pelo usuário (5, 10 ou 25)
            continue #Reinicie o loop

    #Ao sair do loop (quando saldo for menor que 0)
    print(f"Change Owed: {abs(saldo_a_pagar)}") #Imprima o valor final da variável (saldo_a_pagar)
    #A função abs() serve para nos retornar um valor absoluto, por mais que a variável termine com valor negativo, a função abs() torna ela um valor real

#Chamando a função main()
main()