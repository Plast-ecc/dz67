try:
    N = int(input("Введите число N: "))
    
    t = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke

    for i in range(1, N+1):
        t *= i
    print(f"{N}! = {t}")

except:
    print("Ошибка: неверные исходные данные")