def hello():
    word = input("Greeting: ")

    if "Hello" in word:
        print("$0")

    elif word[0] == "W":
        print("$100")

    else:
        print("$20")

hello()


