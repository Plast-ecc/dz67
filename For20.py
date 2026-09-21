try:
    N = int(input("Введите число N: "))

    s = 0
    t = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(1, N+1):
        t *= i
        s +=
        print(f"Сумма будет равна {s}")

except:
    print("Ошибка: неверные исходные данные")