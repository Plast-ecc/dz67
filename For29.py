try:
    N = int(input("Введите число N (> 1): "))
    A = float(input("Введите число A: "))
    B = float(input("Введите число B: "))

    if N <= 1:
        print("N должно быть больше 1")
        broke

    elif A >= B:
        print("A должно быть меньше B")
        broke

    H = (B-A)/N
    print("H =", H)
    for i in range(N+1):
        print(A+i*H)

except:
    print("Ошибка: неверные исходные данные")