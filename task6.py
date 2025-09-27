s = input("Введите строку: ").lower()
vowels = "аеёиоуыэюяaeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Количество гласных:", count)
