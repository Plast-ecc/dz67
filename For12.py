try:
    N = int(input("Введите число N: "))

    s = 1

    if N <= 0:
        print("N должно быть больше 0")
        broke
        
    for i in range(1, N + 1):
        s *= 1 + i / 10
        print(f"Поизведение будет равнo {s}")

except:
    print("Ошибка: неверные исходные данные")