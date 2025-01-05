import os
from pathlib import Path

# Определяем BASE_DIR так же, как в settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

# Путь к папке static
static_path = os.path.join(BASE_DIR, "personal_assistant", "static")
print(f"BASE_DIR: {BASE_DIR}")
print(f"STATICFILES_DIRS Path: {static_path}")

# Проверяем, существует ли папка static
if os.path.exists(static_path):
    print("Папка static найдена!")
else:
    print("Папка static не найдена.")
