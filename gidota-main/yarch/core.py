"""
Модуль который хранит главные функции
"""
from utils import check_confirm


def delete_tasks(task_collection):
    """Удаление задачи по номеру"""
    delete_task = input("Введите номер задачи: ").strip()

    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task} удалена!")
    else:
        print("Неверный номер задачи!")


def edit_task(task_collection):
    """Редактирование задачи по номеру"""
    edit_task_number = input("Введите номер задачи: ").strip()
    if check_confirm(edit_task_number, task_collection):
        new_name = input("Новое имя задачи: ").strip()
        new_content = input("Новое содержание задачи: ").strip()
        if not new_name:
            print("Имя задачи не может быть пустым!")
            return
        task_collection[int(edit_task_number) - 1] = f"{new_name} | {new_content}"
        print(f"Задача {edit_task_number} успешно изменена!")
    else:
        print("Неверный номер задачи!")


def add_task(task_collection):
    """Добавление новой задачи"""
    task_name = input("Введите имя задачи для добавления: ").strip()
    task_content = input("Введите содержание задачи: ").strip()

    if not task_name:
        print("Имя задачи не может быть пустым!")
        return

    full_task = f"{task_name} | {task_content}"
    task_collection.append(full_task)
    print(f"Задача «{task_name}» успешно добавлена!")
