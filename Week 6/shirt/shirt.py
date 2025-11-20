import os
import sys
arquivo = 'foto.jpg'
nome, extensao = os.path.splitext(arquivo)

extensao = extensao.lower()

#print(nome)
#print(extensao)

extensao_valida = ['.jpg', '.jpeg', '.png']

if extensao not in extensao:
    sys.exit("Arquivo de entrada inválido. Use JPG ou PNG.")
else:
    sys.exit("Extensão aceita")

