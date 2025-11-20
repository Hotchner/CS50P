import numpy as np #Importando a biblioteca numpy para criar um range de números float

def main(): #Criando a função principal

    #Definindo horários de cada refeição
    breakFastTime = np.arange(7.0, 8.0, 0.1)
    lunchTime = np.arange(12.0, 14.0, 00.1)
    dinnerTime = np.arange(18.0, 20.0, 00.1)

    #Solicitando o horário
    currentTime = input("What time is it? ")


    if is_close(convert(currentTime), breakFastTime):
        print("breakfast time")

    elif is_close(convert(currentTime), lunchTime):
        print("lunch time")

    elif is_close(convert(currentTime), dinnerTime):
        print("dinner time")

#Função que verifica se o valor inserido (value) existe em algum dos horários (target_times)
def is_close(value, target_times, tolerance=0.05): #Essa função recebe dois argumentos (value & uma lista (target_times))
    for target_time in target_times: #Para cada item (target_time) de uma lista (target_times)..
        if abs(value - target_time) <= tolerance: #Se o valor absoluto entre a subtração: valor - target_time for igual ou menor que o valor da tolerâcia, retorne True
            return True
    return False

#Convertendo horas em valores float
def convert(time): #Criando a função que faz essa conversão de string para número
    horas, minutos = time.split(":") # Utilizando o método split() para atribuir os valores captados nas variáveis horas e minutos

    horasF = float(horas) #Convertendo as horas em Float
    minutosF = float(minutos) #Convertendo os minutos em Float
    minutosF2 = minutosF / 60 #Transformando os minutos em números de 1 a 10, exemplo: 7 horas e 30 minutos = 7,5 horas
    finalHour = minutosF2 + horasF #Somando os minutos as horas para retornarmos as horas no formato esperado

    return round(finalHour, 2) #Retornando as horas e formando com 2 casas decimais através da função round()

if  __name__ == "__main__":
   main()
