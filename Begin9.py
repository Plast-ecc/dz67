import math

a = int(input("Введите первое неотрицательное число: "))
b = int(input("Введите втооре неотррицательное число: "))

if a >= 0 and b >= 0:
    geomMean = math.sqrt(a*b)
    print(f"Среднее геометрическое будет равно {geomMean}")
else:
    print("Оба числа должны быть неотрицательными")
