import os

# Указываем путь к директории
path = input("Введите путь к папке с файлами: ")
# или
# path = r"D:\Programming\python\star\star\media\documents"

# Получаем название папки
directory = os.path.basename(path)
# Получаем список файлов
files = os.listdir(path)
# Будущий результат
res = "python manage.py shell\n"
res += f"from docs.models import {directory.capitalize()}\n{directory.capitalize()}.objects.all()\n"

for file in files:
    filename = "".join(file.split(".")[:-1])  # Убираем расширение файла
    if directory == "documents":
        res += f'{directory.capitalize()}(name_document = "{filename}",' \
               f' file_doc = "{os.path.join(directory, file)}").save()\n'
    elif directory == "applications":
        res += f'{directory.capitalize()}(name = "{filename}",' \
               f' file_app = "{os.path.join(directory, file)}").save()\n'
    else:
        raise ValueError("Ошибка! Возможно указан неверный путь.")

res += f"{directory.capitalize()}.objects.all()\nexit()\npython manage.py runserver"

# Выводим необходимый код со списком файлов
print(res)
