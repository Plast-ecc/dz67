try:
    N = int(input("Введите число N: "))

    if N <= 0:
        broke

    s = 0

    for i in range(1, N+1):
        s += i ** (N-i+1)

    print(f"Сумма будет равна {s}")

except:
    if N <= 0:
        print("N должно быть больше 0")
    
    else:
        print("Ошибка: неверные исходные данные")