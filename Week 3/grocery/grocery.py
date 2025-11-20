def main():
    carrinho = {}

    while True:
        try:
            produto = input("").lower()

            if not carrinho:
                carrinho.update({f'{produto}': 1})
                continue

            elif produto in carrinho:
                carrinho[f'{produto}'] +=1
                continue

            else:
                carrinho.update({f'{produto}': 1})
                continue

        except EOFError:
            carrinho_ordenado = sorted(carrinho)
            for _ in carrinho_ordenado:
                print(f"{carrinho[f'{_}']} {_.upper()}")
            break

if __name__ =="__main__":
    main()
