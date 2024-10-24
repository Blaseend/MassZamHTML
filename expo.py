import json


def convert_log_to_json(log_file_path, json_file_path):
    # Словарь для хранения 
    data = {}
    current_file = None  # Текущее имя 
    
   
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        # Читаем построчно
        for line in log_file:
            # Проверяем, если это строка с началом файла
            if line.startswith('----------------------------------------------') and 'Конец' not in line:
                # Извлекаем имя файла, убираем разделители
                current_file = line.replace('----------------------------------------------', '').replace('----------------------------------', '').strip()
                data[current_file] = {}  # Создаем запись для нового файла
            
            # Проверяем, если это строка с концом файла
            elif line.startswith('----------------------------------------------Конец'):
                current_file = None  # Заканчиваем запись для текущего файла
            
            
            elif current_file and ': ' in line:
                line_number, text = line.split(': ', 1)
                data[current_file][line_number.strip()] = text.strip()
    

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Данные успешно преобразованы в файл {json_file_path}")


log_file_path = 'log.txt'


json_file_path = 'output.json'


convert_log_to_json(log_file_path, json_file_path)
