my_list = [
    7,
    5,
    3,
    3,
    2
]

newPoint = int(input('Введите новый балл для рейтинга: '))

for index, value in enumerate(my_list):
    if value < newPoint:
        my_list.insert(index, newPoint)
        break

print(my_list)
