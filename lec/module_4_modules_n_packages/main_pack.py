# Мы можем использовать "from" и "*"
# from my_packages import *


# multy_hello('Иван', 'ru')
# multy_hello('Ivan', 'en')

# Через эту же конструкцию мы можем импортировать конкретные функции которые добавлены по умолчанию не обращаясь к конкретному пакету

from my_packages import multy_hello as mul_greeting

mul_greeting('Иван', 'ru')
mul_greeting('Ivan', 'en')


print(f'{globals()}')