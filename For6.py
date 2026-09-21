try:
    pr = float(input("Введите цену 1 кг конфет: "))

    if pr <= 0:
        broke

    for i in range(12, 21, 2):
        w = i/10
        print(f"{w} кг = {pr*w} руб")

except:
    
    if pr < 0:
        print("Цена не может быть отрицательной")
    
    elif pr == 0:
        print("Цена не может быть равна 0")

    else:
        print("Ошибка: неверные исходные данные")