try:
    X = float(input("Введите число X: "))
    N = int(input("Введите число N: "))

    s = 1
    term = 1
    sign = -1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    for i in range(1, N+1):
        term *= X*X / ((2*i-1) * (2*i))
        s += sign*term
        sign = -sign
    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")