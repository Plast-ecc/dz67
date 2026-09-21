try:
    A = int(input("Введите число A (A > 0): "))
    B = int(input("Введите число B (B > A): "))

    if A >= B:
        broke

    elif A == 0:
        broke


    for i in range(A, B +1):
        print((str(i) + " ") * i)

except:
    if A >= B:
        print("B должно быть больше A")
    
    elif A < 0:
        print("A должно быть больше 0")
    else:
        print("Ошибка: неверные исходные данные")