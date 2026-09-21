try:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B (B > A): "))

    s = 1

    if A > B:
            print("A должно быть меньше В")
            broke

    for i in range(A, B + 1):
        s *= i
        print(f"Произведение всех целых чисел от A до B включительно будет равно {s}")

except:
    print("Ошибка: неверные исходные данные")