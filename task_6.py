continueInput = "y"
products = []

name = "название"
price = "цена"
count = "количество"
units = "ед"

while not continueInput == "n":
    productName = input('Введите название товара: ')
    productPrice = int(input('Введите цену товара: '))
    productCount = int(input('Введите количество товара: '))
    productUnit = input('Введите единицы измерения товара: ')

    productNumber = len(products) + 1
    productDict = {
        name: productName,
        price: productPrice,
        count: productCount,
        units: productUnit
    }

    products.append(
        (
            productNumber,
            productDict
        )
    )

    continueInput = input('Добавить еще товар y/n: ')

else:
    my_products_names = []
    my_products_prices = []
    my_products_counts = []
    my_products_units = []

    for i in products:
        product_dict = i[1]
        my_products_names.append(product_dict[name])
        my_products_prices.append(product_dict[price])
        my_products_counts.append(product_dict[count])
        my_products_units.append(product_dict[units])

    my_analytics = {
        name: my_products_names,
        price: my_products_prices,
        count: my_products_counts,
        units: my_products_units
    }

    print(products)
    print()
    print(my_analytics)
