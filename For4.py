try:
    pr = float(input("Введите цену 1 кг конфет: "))

    if pr <= 0:
        broke

    for i in range(1, 11):
        print(f"{i} кг = {pr*i} руб")

except:
    
    if pr < 0:
        print("Цена не может быть отрицательной")
    
    elif pr == 0:
        print("Цена не может быть равна 0")

    else:
        print("Ошибка: неверные исходные данные")