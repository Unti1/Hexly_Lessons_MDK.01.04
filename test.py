result_lst = []


while True:
    x = int(input('Введите число: '))

    if x == 0:
        print('Цикл завершен')
        break
    
    if x % 2 == 0 and (x % 4 == 0 and x % 6 == 0):
        print(f'Чётное число кратное 4 и 6: {x}')
        result_lst.append(x)

print(f'Результат: {result_lst=}')


