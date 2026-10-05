"""
Модуль который загружает и сохраняет задачи
"""
from config import NAME_FILE_SAVES


def load_file(task_list):
    """Загрузить задачи из файла в список"""
    try:
        with open(NAME_FILE_SAVES, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    task_list.append(line)
    except FileNotFoundError:
        pass  # файла ещё нет — просто пустой список
    return task_list


def save_file(task_list, file_name=None):
    """Сохранить список задач в файл"""
    if file_name is None:
        file_name = NAME_FILE_SAVES
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(f"{task.strip()}\n")
