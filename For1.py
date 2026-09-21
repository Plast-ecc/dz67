try:
    N = int(input("Введите N (N > 0): "))
    K = int(input("Введите K: "))

    if N <= 0:
        print("Число N должно быть > 0")

    for i in range(N):
        print(K)

except:
    print("Ошибка: неверные исходные данные")