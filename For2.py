try:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B (B > A): "))
    N = 0

    if A > B:
        print("A должно быть бменьшеольше В")
        broke

    for i in range(A, B + 1):
        print(i)
        N += 1

    print(f"Всего количество чисел равно {N}")

except:
    print("Ошибка: неверные исходные данные")