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
