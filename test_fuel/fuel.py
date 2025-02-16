# def main():
#     print(gauge(convert()))


# def convert():
#     while True:
#         try:
#             frac = input("Fraction: ")

#             x, y = frac.split('/')
#             x, y = int(x), int(y)

#             if x <= y:
#                 result = int(x/y*100)
#                 break
#             elif x > y:
#                 raise ValueError

#         except (ValueError, ZeroDivisionError):
#             continue
#     return result


# def gauge(percentage):
#     if percentage <= 1:
#         return "E"
#     elif percentage >= 99:
#         return "F"
#     else:
#         return f"{percentage}%"

# if __name__ == "__main__":
#     main()

def main():
    print(gauge(convert("2/4")))


def convert(frac):
    while True:
        try:
            # frac = input("Fraction: ")

            x, y = frac.split('/')
            x, y = int(x), int(y)

            if x <= y:
                result = int(x/y*100)
                break
            elif x > y:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            continue
    return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
