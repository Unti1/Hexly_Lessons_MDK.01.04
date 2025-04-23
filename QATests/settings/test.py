import os

print(f'{__file__=}')
print(f'{os.path.dirname(__file__)=}')
print(f'{os.path.split(os.path.dirname(__file__))=}')
print(f'{os.path.split(os.path.dirname(__file__))[0]=}')
print(f'{os.path.join(os.path.split(os.path.dirname(__file__))[0], ".env")=}')
