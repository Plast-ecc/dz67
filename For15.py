try:
    A = float(input("Введите число A: "))
    N = int(input("Введите число N: "))
    
    result = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(N):
        result *= A
    print(f"{A}^{N} = {result}")

except:
    print("Ошибка: неверные исходные данные")