try:
    N = int(input("Введите число N (> 1): "))

    if N < 1:
        print("N должно быть больше 1")
        broke
        
    a1, a2 = 1, 2

    print(a1, a2, end=" ")

    for k in range(3, N+1):
        a3 = (a1+2*a2) / 3
        print(a3, end=" ")
        a1, a2 = a2, a3

except:
    print("Ошибка: неверные исходные данные")