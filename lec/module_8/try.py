import traceback


def func1():
    try:
        print('Запуск основной функции')
        return func2()
    except Exception as e:
        print(traceback.format_exc())
    # except ValueError as e:
    #     print('Возникла ошибка и обратана func1: ', e)
    finally:
        print('Завершение основной функции')

def func2():
    print('Запуск вложенной функции func2')
    result = func3()
    print('Завершение вложенной функции func2')
    return result

def func3():
    print('Запуск 3тей вложенной функции func3')
    raise ValueError('Это ошибка из 3тей функции')

func1()