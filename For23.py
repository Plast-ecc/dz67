try:
    X = float(input("Введите число X: "))
    N = int(input("Введите число N: "))

    s = 0
    term = X
    sign = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    for i in range(0, N+1):
        s += sign*term
        term *= X*X / ((2*i+2) * (2*i+3))
        sign = -sign
    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")