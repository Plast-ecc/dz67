try:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B (B > A): "))
    N = 0

    if A > B:
        print("A должно быть меньше В")
        broke

    for i in range(B - 1, A, -1):
        print(i)
        N += 1

    print(f"Количество чисел между А и В равно {N}")

except:
    print("Ошибка: неверные исходные данные")