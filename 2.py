path = input("шлях до txt файлу ")

try:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        print("вміст")
        print(content)
except FileNotFoundError:
    print("файл не знайдено")
