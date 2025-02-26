def ru_hello(name):
    print(f"Привет, {name}!")
    
def en_hello(name):
    print(f"Hello, {name}!")
    
def multy_hello(name, lang):
    if lang == "ru":
        ru_hello(name)
    elif lang == "en":
        en_hello(name)
    else:
        print("Я не знаю такой языка!")
