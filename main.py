import os


def find_obuch_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        matches = []
        for line_number, line in enumerate(lines, start=1):
            if "ХХХ".lower() in line.lower():
                matches.append(f"{line_number}: {line.strip()}")
        
        return matches
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")
        return []

# Основная функ
def process_html_files(folder_path, log_file):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            matches = find_obuch_in_file(file_path)
            
            if matches:
                log_file.write(f"----------------------------------------------{file_name}----------------------------------\n")
                for match in matches:
                    log_file.write(f"{match}\n")
                log_file.write(f"----------------------------------------------Конец {file_name}----------------------------------\n\n")


folder_path = os.path.dirname(os.path.abspath(__file__))


with open('log.txt', 'w', encoding='utf-8') as log_file:
    process_html_files(folder_path, log_file)

print("Поиск завершен. Результаты записаны в log.txt.")
