try:
    X = float(input("Введите число X (|X| < 1): "))
    N = int(input("Введите число N: "))

    s = 0.0
    term = X
    sign = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    elif abs(X) >= 1:
        print("|X| должно быть меньше 1")
        broke

    for i in range(0, N+1):
        s += sign*term / (2*i+1)
        term *= X*X
        sign = -sign
    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")