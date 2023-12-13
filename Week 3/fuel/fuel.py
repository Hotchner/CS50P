def main():
    x = get_fuel()

    if x in range(99, 101):
        print("F")
    elif x in range(0, 2):
        print("E")
    else:
        print(f"{x}%")

    

def get_fuel():

    while True:
        x = input("Fraction: ")

        n1, n2 = x.split("/")
        n1, n2 = int(n1), int(n2)

        _ = round((n1/n2) * 100)
        
        if _ > 100:
            continue
        else:
            return _

    
while True:
    try:
        main()
        break
    except (ValueError, ZeroDivisionError):
        continue
    