import inflect
pl = inflect.engine()

def main():
    try:
        peoples_list =[]

        while True:
            people = input("Name: ")
            peoples_list.append(people)
            continue
    except (EOFError):
        peoples_list = pl.join(peoples_list)
        print(f"Adieu, adieu, to {peoples_list}")

main()
