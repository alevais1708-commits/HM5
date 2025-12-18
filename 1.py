while True:
 try:
    number = int(input("ведіть число "))
    print(f"число {number}")
 except ValueError:
    print("помилка")
