a = int(input("Введите первое ненулевое число: "))
b = int(input("Введите второе ненулевое число: "))

if a != 0 and b != 0:
    module_a = abs(a)
    module_b = abs(b)
    print(f" Сумма модулей будет равна {module_a+module_b} \n Разность модулей будет равна {module_a-module_b} \n Произведение модулей будет равно {module_a*module_b} \n Частное модулей будет равно {module_a/module_b}")

else:
    print("Числа должны быть ненулевыми")