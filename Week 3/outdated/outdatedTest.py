n = 2

# print(f"{n:02}")

month1 = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# print(month1[1])

# date = input("Date: ")

# month, day, year = date.split("/")
# month = int(month)
# day = int(day)

# print(f"{year}-{month:02}-{day:02}") 

# print(f"{month1[month]} {day:02} {year}")

# imprimir indice no lugar do mes

# month_day, year = date.split(",")

# year2 = year.strip()

# mes, dia = month_day.split(" ")

# print(dia)
# print(mes)
# print(year2)
print("-" *10)
# print(f"{year2}-{month1.index(f"{mes}")+1:02}-{int(dia):02}")

# print(month1.index("September"))



abc = "1/9/2002"

dia, mes, ano = abc.split("/")

print(f"{int(dia):02}, {int(mes):02}, {ano}")

#Up