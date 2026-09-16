import math

try:
    x1 = int(input("Введите x1: "))
    y1 = int(input("Введите y1: "))
    x2 = int(input("Введите x2: "))
    y2 = int(input("Введите y2: "))

    rastoyanie = math.sqrt((x2-x1)**2+(y2-y1)**2)

    print(f"Расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости будет равно {rastoyanie}")

except:
    print("Ошибка: Число некоректное")