try:
    N = int(input("Введите число N: "))

    s = 1
    f = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    for i in range(1, N+1):
        f *= i
        s += 1/f
    print(f"Сумма будет равна {s}")
    print("exp(1) ≈", 2.718281828459045)

except:
    print("Ошибка: неверные исходные данные")