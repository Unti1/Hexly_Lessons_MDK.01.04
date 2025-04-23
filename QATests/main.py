# 1 способ вызова логера (глобальный)
# from settings.loggers import *

# logging.info('Starting the application...')
# logging.warning('Warn...')
# logging.error('Error...')

# 2 способ вызова логера (локальный)
import traceback
from settings.config import settings
from settings.loggers import app_logger
# app_logger.info('Starting the application...')
# app_logger.warning('Warn...')
# app_logger.error('Error...')
# app_logger.error('Поблема...')

def func(x,y):
    try:
        return x/y, 'Успех'
    except ZeroDivisionError as e:
        return 0, 'Успех'
    except Exception as e:
        app_logger.error(traceback.format_exc())
        return None, f'Ошибка: {e}'

print(f'{func(10,0)=}')
print(f'{func("a",0)=}')


# print(settings)
print(settings.AUTHOR)
print(settings.PG_DB)

    