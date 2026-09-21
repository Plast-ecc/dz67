try:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B (B > A): "))

    s = 0

    if A > B:
            print("A должно быть меньше В")
            broke

    for i in range(A, B + 1):
        s = i**2
        print(f"Сумма кводратов всех целых чисел от A до B включительно будет равна {s}")

except:
    print("Ошибка: неверные исходные данные")