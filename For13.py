try:
    N = int(input("Введите число N: "))

    s = 0
    d = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(1, N + 1):
        s += d*(1+i/10)
            d = -d
        print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")