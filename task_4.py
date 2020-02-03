my_string = input('Введите любую строку: ')

my_list = my_string.split(" ")

for index, value in enumerate(my_list):
    if len(value) > 10:
        value = value[0:10]
    print(f"{index + 1}. " f"{value}" "\n")
