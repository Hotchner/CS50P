conta = input("Expression: ")

x, y, z = conta.split(" ")

def calculadora(x, y, z):
    if y == "+":
        return float(x) + float(z)
    
    elif y == "-":
        return float(x) - float(z)
    
    elif y == "*":
        return float(x) * float(z)

    elif y == "/":
        return float(x) / float(z)
    

print(calculadora(x, y, z))

