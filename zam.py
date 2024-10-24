import json
import os


def replace_lines_in_html(json_file_path):
  
    current_folder = os.path.dirname(os.path.abspath(__file__))

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)


    for file_name, lines_to_replace in data.items():
        file_path = os.path.join(current_folder, file_name)  


        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден.")
            continue


        with open(file_path, 'r', encoding='utf-8') as html_file:
            lines = html_file.readlines()


        for i, line in enumerate(lines, start=1):
            line_number_str = str(i)
            if line_number_str in lines_to_replace:
                # Сохраняем отступы перед строкой
                leading_whitespace = len(line) - len(line.lstrip())
                new_text = lines_to_replace[line_number_str].strip()

                # Заменяем строку с учётом отступов
                lines[i - 1] = ' ' * leading_whitespace + new_text + '\n'

        # Записываем изменения обратно в HTML файл
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.writelines(lines)

        print(f"Строки в файле {file_name} успешно заменены.")


json_file_path = 'output.json'


replace_lines_in_html(json_file_path)
