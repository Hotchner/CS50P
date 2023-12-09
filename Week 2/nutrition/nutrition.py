fruits = [

     {"fruit_name": "Apple",
     "Calories": "130"},

     {"fruit_name": "Avocado",
     "Calories": "50"},

     {"fruit_name": "Banana",
     "Calories": "110"},

     {"fruit_name": "Cantaloupe",
     "Calories": "50"},

     {"fruit_name": "Grapefruit",
     "Calories": "60"},

     {"fruit_name": "Grapes",
     "Calories": "90"},

     {"fruit_name": "Honeydew Melon",
     "Calories": "50"},

     {"fruit_name": "Kiwifruit",
     "Calories": "90"},

     {"fruit_name": "Lemon",
     "Calories": "15"},

     {"fruit_name": "Lime",
     "Calories": "20"},

     {"fruit_name": "Nectarine",
     "Calories": "60"},

     {"fruit_name": "Orange",
     "Calories": "80"},

     {"fruit_name": "Peach",
     "Calories": "60"},

     {"fruit_name": "Pear",
     "Calories": "100"},

     {"fruit_name": "Pineapple",
     "Calories": "50"},

     {"fruit_name": "Plums",
     "Calories": "70"},

     {"fruit_name": "Strawberries",
     "Calories": "50"},

     {"fruit_name": "Sweet Cherries",
     "Calories": "100"},

     {"fruit_name": "Tangerine",
     "Calories": "50"},

     {"fruit_name": "Watermelon",
     "Calories": "80"}
]

def main():
    fruit_selected = input("Item: ").lower()

    for fruit in fruits:
        if fruit["fruit_name"].lower() == fruit_selected:
            print(f"Calories: {fruit["Calories"]}")


main()