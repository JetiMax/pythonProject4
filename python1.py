import os
import shutil
from os import path


def main():
    # сделать дубликат существующего файла
    if path.exists("junior.txt"):
        # получить путь к файлу в текущем каталоге
        src = path.realpath("junior.txt");

        # переименовываем исходный файл
        os.rename('junior.txt', 'middle.txt')


if __name__ == "__main__":
    main()

