"""
Модуль для хранения конфигураций
"""
import os.path
from utils import get_base_dir

collection = []
is_running = True
NAME_FILE_SAVES = os.path.join(get_base_dir(), "saves.txt")
