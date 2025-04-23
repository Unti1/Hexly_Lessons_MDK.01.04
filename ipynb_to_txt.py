import json
import argparse
import os

def convert_ipynb_to_txt(ipynb_path, txt_path=None):
    txt_path = os.path.split(ipynb_path)[-1]
    txt_path = txt_path.replace('.ipynb', '.txt')
    try:
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {ipynb_path} не найден.")
        return
    except json.JSONDecodeError:
        print("Ошибка: Некорректный JSON-формат.")
        return

    output = []
    for cell in notebook.get('cells', []):
        cell_type = cell.get('cell_type')
        source = cell.get('source', [])
        
        # Объединяем строки ячейки в один текст
        content = ''.join(source).strip()
        
        if cell_type == 'markdown':
            output.append('## Markdown\n' + content + '\n')
        elif cell_type == 'code':
            output.append('## Code\n```python\n' + content + '\n```\n')

    try:
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output))
        print(f"Успешно сохранено в {txt_path}")
    except IOError:
        print(f"Ошибка: Не удалось записать в {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Конвертирует Jupyter Notebook в TXT с блоками Markdown и Code.')
    parser.add_argument('input', help='Путь к .ipynb файлу')
    # parser.add_argument('output', help='Путь к выходному .txt файлу')
    args = parser.parse_args()
    convert_ipynb_to_txt(args.input)