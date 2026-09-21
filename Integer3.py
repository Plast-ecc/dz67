try:
    b = float(input("Введите размер файла в байтах: "))

    baity_v_kilb = b//1024

    if b > 0 and b < 2:
        print(f"В полных килобайтах 1 байт будет равен {baity_v_kilb}")

    elif b <= 0:
        print("Ошибка: неверные исходные данные")

    else:
        print(f"В полных килобайтах {b} Б будут равны {baity_v_kilb} КБ")

except:
    print("Ошибка: неверные исходные данные")