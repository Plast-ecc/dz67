try:
    X = float(input("Введите число X (|X| < 1): "))
    N = int(input("Введите число N: "))

    s = X
    term = X

    if N <= 0:
        print("N должно быть больше 0")
        broke

    elif abs(X) >= 1:
        print("|X| должно быть меньше 1")
        broke

    for i in range(1, N + 1):
        term *= (2*i-1) * X*X / ((2*i)*(2*i+1))
        s += term
    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")