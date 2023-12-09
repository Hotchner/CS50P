# print(round(5/4 * 100))


# if x in e:
#         print("E")

#     elif x in f:
#         print("F")

#     elif x > 100:
#         return False

#     else:
#         print(f"{x}%")


# x = input("Fraction: ")

#     n1, n2 = x.split("/")
#     n1, n2 = int(n1), int(n2)

#     return round((n1/n2) * 100)

f = range(99, 101)

for _ in f:
    print(_)

while True:
    try:
        main()
        break
    except (ValueError, ZeroDivisionError):
        continue

# if _ > 100:
#         get_fuel()
#     else:
#         return _