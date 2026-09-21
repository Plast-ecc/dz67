try:
    N = int(input("Введите число N: "))

    a = 1.0

    if N <= 0:
        print("N должно быть больше 0")
        broke

    for k in range(1, N+1):
        a = (a+1)/k
        print(f"A{k} = {a}")

except:
    print("Ошибка: неверные исходные данные")