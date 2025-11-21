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

def main():

    date = input("Date: ").strip()

    if "/" in date:
        print(slash_date(date))

    elif "," in date:
        print(comma_date(date))

    else:
        raise ValueError



def slash_date(text):
    month, day, year = text.split("/")
    day = int(day)
    month = int(month)

    if day in range(0, 32) and month in range(0, 13):
        return f"{year}-{month:02}-{day:02}"

    else:
        raise ValueError

def comma_date(text):
    month_day, year = text.split(",")
    month, day = month_day.split(" ")
    day = int(day)

    if day in range(0, 32) and month in month1:
        return f"{year.strip()}-{month1.index(month)+1:02}-{int(day):02}"

    else:
        raise ValueError

while True:
    try:
        main()
        break
    except ValueError:
        continue
