my_list = [
    1,
    4,
    7,
    True,
    False,
    "Python",
    ['a', 'd', 'c'],
    "Msk",
    220
]

for index, element in enumerate(my_list):
    if index % 2 == 1:
        my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]

print(my_list)
