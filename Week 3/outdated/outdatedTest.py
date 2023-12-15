n = 2

print(f"{n:02}")

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

print(month1[1])

date = input("Date: ")

month, day, year = date.split("/")
month = int(month)
day = int(day)

print(f"{year}-{month:02}-{day:02}") 

print(f"{month1[month]} {day:02} {year}")