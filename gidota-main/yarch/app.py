"""

"""
import sys
import os

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def insure_save_file(filename="save.json"):
    base_dir = get_base_dir()
    save_path = os.path.join(base_dir, filename)

    if not os.path.exists(save_path):
        with open(save_path, "w", encoding="utf-8") as f:
            f.write("{}")
        print(f"Файл сохранений создан: {save_path}")

    return save_path

from config import is_running, NAME_FILE_SAVES, collection
from view import show_collection, show_menu
from core import delete_tasks, edit_task, add_task
from storage import load_file, save_file
from utils import insure_saves_file



def app():
    insure_saves_file()
    global is_running

    # Загружаем задачи при старте
    load_file(collection)

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ").strip()

        match choice_user:
            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_file(collection)

            case "3":
                show_collection(collection)
                edit_task(collection)
                save_file(collection)

            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_file(collection)

            case "5":
                save_file(collection)
                is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")