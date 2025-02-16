def main():
    twttr = input("Twttr: ").lower()
    return print(shorten(twttr))

def shorten(word):
    wovels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    # wovels = ["a", "e", "i", "o", "u"]
    new_word = ""

    for _ in word:
        if _ in wovels:
            pass
        else:
            new_word = new_word + _
    return new_word

if __name__ == "__main__":
    main()
