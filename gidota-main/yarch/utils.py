"""
Модуль который содержит утилиты
"""
import os
import sys

from config import NAME_FILE_SAVES


def check_confirm(select_task, task_list):
    """Проверка, что введён корректный номер задачи"""
    if select_task.isdigit():
        if 0 < int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print("Введите именно номер задачи!")
        return False
def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))
def insure_saves_file():
    if not os.path.exists(NAME_FILE_SAVES):
        with open(NAME_FILE_SAVES, "w", encoding="utf-8") as saves_file:
            return NAME_FILE_SAVES
