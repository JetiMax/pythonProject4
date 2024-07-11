import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive


def main2():
    # Проверить, существует ли файл
    if path.exists("middle.txt"):
        # получить путь к файлу в текущем каталоге
        src = path.realpath("middle.txt");
        # помемещаем все в ZIP-архив
        root_dir,tail = path.split(src)
        shutil.make_archive("middle_archive", "zip", root_dir)


if __name__== "__main__":
    main2()

    //