import random

def main():
    tentativas = 0
    acertos = 0

    level = get_level()

    while tentativas < 10:
        try:
            a, b = generate_integer(level), generate_integer(level)

            result = a + b

            resposta = int(input(f"{a} + {b} = "))

            if resposta == result:
                tentativas += 1
                acertos += 1
                continue
            else:
                raise ValueError

        except (ValueError):
            print("EEE")
            erros = 1

            while True:
                try:
                    resposta = int(input(f"{a} + {b} = "))

                    if resposta == result:
                        tentativas += 1
                        acertos += 1
                        break

                    elif resposta != result and erros < 2:
                        erros += 1
                        print("EEE")
                        continue

                    else:
                        tentativas += 1
                        print(f"{a} + {b} = {a+b}")
                        break
                except(ValueError):
                   if erros < 2:
                        erros += 1
                        print("EEE")
                        continue
                   else:
                        tentativas += 1
                        print(f"{a} + {b} = {a+b}")
                        break

    return print(f"Score: {acertos}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                break
            else:
                continue
        except(ValueError):
            continue
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
