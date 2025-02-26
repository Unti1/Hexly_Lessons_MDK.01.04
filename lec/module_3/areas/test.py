inv = {}

def add_item(item: str, quantity: int):
    if item in inv:
        inv[item] += quantity
    else:
        inv[item] = quantity

def remove_item(item: str, quantity: int):
    if item in inv:
        if inv[item] >= quantity:
            inv[item] -= quantity
        else:
            print(f'Ошибка: недостаточно {item} на складе')
    else:
        print(f"Ошибка: {item} отсутствует на складе")

def display_inventory():
    print('Склад', end='\n\n')
    for item, quantity in inv.items():
        print(f"{item}: {quantity}")
    print()

if __name__ == "__main__": # Если файл который мы запускаем, является ГЛАВНЫМ или ОСНОВНЫМ ЗАПУСКАЕМЫМ то выполняем код под условием
    print(f'{inv=}')
    add_item("Яблоки",50)
    add_item("Бананы",30)
    display_inventory()
    remove_item("Яблоки",30)
    display_inventory()
    remove_item("Груши",10)
    print(f'{inv=}')
