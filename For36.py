try:
    N = int(input("Введите число N: "))
    K = int(input("Введите число К: "))

    bez_bolishih_chisel = 0

    for z in range(1, N +1):
        bez_bolishih_chisel += int(z**K) 
    print(f"Сумма будет равна {bez_bolishih_chisel}")  

except:
    print("Ошибка: неверные исходные данные")