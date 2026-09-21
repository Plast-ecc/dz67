try:
    N = int(input("Введите число N (> 0): "))

    if N <= 0:
        broke

    s = 0

    for i in range(1, N+1):
        t = i ** i
        s += t
    print(f"Сумма будет равна {s}")

except:
    if N <= 0:
        print("N должно быть больше 0")
    
    else:
        print("Ошибка: неверные исходные данные")