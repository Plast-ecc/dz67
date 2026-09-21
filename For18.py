try:
    A = float(input("Введите число A: "))
    N = int(input("Введите число N: "))
    
    s = 1
    d = 1
    p = -1

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(N):
        d *= A
        s += p*d
        p = -p
    print(f"Значение будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")