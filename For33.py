try:
    N = int(input("Введите число N (> 1): "))

    f1, f2 = 1, 1

    if N <= 1:
        print("N должно быть больше 1")
        broke

    print(f"F1 = {f1}")
    print(f"F2 = {f2}")

    for i in range(3, N + 1):
        f1, f2 = f2, f1 + f2
        print(f"F{i} = {f2}")

except:
    print("Ошибка: неверные исходные данные")