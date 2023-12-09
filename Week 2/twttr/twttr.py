def remove_letter():

    wovels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    word = input("Input: ")
    new_word = ""

    for letter in word:
        if letter in wovels:
            letter.replace(letter, "")
        else:
            new_word = new_word + letter
    return print(new_word)

remove_letter()

            