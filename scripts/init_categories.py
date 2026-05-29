import sys
sys.path.append(".")

from scripts.seed_data import seed_categories

if __name__ == "__main__":
    print("Инициализация категорий...")
    seed_categories()
    print("Готово!")
