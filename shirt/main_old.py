import sys
import os

if len(sys.argv) !=3:
    sys.exit("Uso: python shirt.py entrada.jpg saida.png")

entrada = sys.argv[1]
saida = sys.argv[2]

print(f"Entrada: {entrada}")
print(f"Saída: {saida}")    

arquivo = ""