import inflect

# #Função que utilizaremos
# mylist = p.join(("apple", "banana", "carrot"))
# # "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# # "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# # "apple, banana and carrot"


pl = inflect.engine()

# print(pl.plural("Coffe"))

# print(pl.singular_noun("Coffes"))

# print(pl.number_to_words(20))

# print(pl.plural("Ana", "Carlos", "Louie"))

def main1():

    peoples = []

    while True:
        item = input("Item: ").title()

        if item in menu:
            total = total + menu[f"{item}"]
            print(f"Total: ${total:.2f}")
            continue

        else:
            print(f"Total: ${total:.2f}")
            continue

# mylist = pl.join(("apple", "banana", "carrot"))

# peoples = []

# print(peoples)

# peoples.append("Ana")
# peoples.append("Carla")
# peoples.append("Pedro")

# print(peoples)

# peoples = pl.join(peoples)
# print(peoples)



def main():
    try:
        peoples_list =[]

        while True:
            people = input("Name: ")
            peoples_list.append(people)
            continue
    except (KeyboardInterrupt):
        peoples_list = pl.join(peoples_list)
        print(f"Adieu, adieu, to {peoples_list}")


main()