# 1
monthNumber = int(input('Введите номер текущего месяца: '))

seasons = [
    "winter",
    "spring",
    "summer",
    "autumn"
]

if 0 < monthNumber < 3 or monthNumber == 12:
    print(seasons[0])
elif 2 < monthNumber < 6:
    print(seasons[1])
elif 5 < monthNumber < 9:
    print(seasons[2])
elif 8 < monthNumber < 12:
    print(seasons[3])
else:
    print("Неправильный номер месяца")

# 2
my_monthNumber = int(input('Введите номер текущего месяца: '))

my_seasons = {
    "winter": {1, 2, 12},
    "spring": {3, 4, 5},
    "summer": {6, 7, 8},
    "autumn": {9, 10, 11}
}

for season, month in my_seasons.items():
    if my_monthNumber in month:
        print(season)
        break
    elif monthNumber > 12 or monthNumber < 1:
        print("Неправильный номер месяца")
        break
