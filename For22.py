try:
    X = float(input("Введите число X: "))
    N = int(input("Введите число N: "))

    s = 1
    term = 1    

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(1, N+1):
        term *= X/i
        s += term
        print(f"Сумма будет равна {s}")

except:
    print("Ошибка: неверные исходные данные")