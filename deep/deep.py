def main():
    reply = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match reply.strip().lower():
        case "42":
            print("Yes")

        case "forty two":
            print("Yes")

        case "forty-two":
            print("Yes")

        case _:
            print("No")
main()
