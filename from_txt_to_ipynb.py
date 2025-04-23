

import json
import argparse
import os

def convert_txt_to_ipynb(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            txt_source = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {txt_path} не найден.")
        return
    except json.JSONDecodeError:
        print("Ошибка: Некорректный JSON-формат.")
        return
    result = {}
    
    cells = []
    splited_text = txt_source.split('---')
    for text in splited_text:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"{text}"
            ]
            })
        
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ваш код тут"
            ]
            })
        
    result.update({
        "cells": cells,
        "metadata": {
                        "language_info": {
                            "name": "python"
                            }
                    },
                    "nbformat": 4,
                    "nbformat_minor": 2
                    })
    ipynb_file = os.path.split(txt_path)[-1].replace('.txt', '.ipynb')
    with open(ipynb_file, 'w', encoding='utf-8') as ipynb_path:
        json.dump(result, ipynb_path)
    
    return ipynb_file

                            
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Конвертирует TXT в Jupyter Notebook с блоками Markdown и Code.')
    parser.add_argument('input', help='Путь к .txt файлу')
    # parser.add_argument('output', help='Путь к выходному .txt файлу')
    args = parser.parse_args()
    convert_txt_to_ipynb(args.input)