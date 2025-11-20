import emoji

def main():
    text = input("Input: ")
    print(emoji.emojize(f'{text}', language='alias'))

main()
