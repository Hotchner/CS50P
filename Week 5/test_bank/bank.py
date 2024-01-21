def main():
    greeting = input("Greeting: ")

    print(value(greeting))


def value(greeting):
    if "hello" in greeting.lower():
        return "$0"
    elif greeting.lower()[0] == "h" and greeting.lower() != "hello":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()