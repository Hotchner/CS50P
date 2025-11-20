expression = input("Expression: ")

x, y, z = expression.split(" ")

def calculator(x, y, z):
    if y == "+":
        return float(x) + float(z)

    elif y == "-":
        return float(x) - float(z)

    elif y == "*":
        return float(x) * float(z)

    elif y == "/":
        return float(x) / float(z)


print(calculator(x, y, z))
