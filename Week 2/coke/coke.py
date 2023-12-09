# O valor da coca é 50C
# A máquina só aceita moedas de 25C, 10C e 5C
# Se forem adicionadas moedas que não são aceitas, o saldo devedor não deve mudar


# captar o valor 

# def main():
#     coins_acepted = [25, 10, 5]

#     coins_to_pay = 50

#     while coins_to_pay <= 0:
        
def main():

    saldo_a_pagar = 50

    coins_acepted = [25, 10, 5]

    while saldo_a_pagar > 0:
        print(f"Amount Due: {saldo_a_pagar}")
        coin_insert = int(input("Insert Coin: "))

        if coin_insert not in coins_acepted:
            continue

        elif coin_insert in coins_acepted:
            saldo_a_pagar = saldo_a_pagar - coin_insert
            continue
    print(f"Change Owed: {abs(saldo_a_pagar)}")
main()



'''
saldo = 5
acepte_keys = [5, 11, 45]

if saldo not in acepte_keys:
    print("Vazio")
else:
    print("Sim")
'''