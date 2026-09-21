try:
    N = int(input("Введите N (> 2): "))

    a1, a2, a3 = 1, 2, 3

    print(a1, a2, a3, end=" ")

    for k in range(4, N+1):
        a4 = a3 + a2-2*a1
        print(a4, end=" ")
        a1, a2, a3 = a2, a3, a4

except:
    print("Ошибка: неверные исходные данные")