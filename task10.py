arr = list(map(int, input("Введите массив чисел через пробел: ").split()))
x = int(input("Введите число для поиска: "))
if x in arr:
    print("Число найдено")
else:
    print("Число не найдено")
