try:
    X = float(input("Введите число X (|X| < 1): "))
    N = int(input("Введите число N: "))

    s = 1.0
    term = 1.0
    sign = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    elif abs(X) >= 1:
        print("|X| должно быть меньше 1")
        broke

    for i in range(1, N+1):
        if i == 1:
            term = X/2
        else:
            term *= (2*i-3) *X/ (2*i)
        s += sign*term
        sign = -sign

    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")