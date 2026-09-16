import math

a = int(input("Введите длину первого катета: "))
b = int(input("Введите длиту второго катета: "))

c = math.sqrt(a*a + b*b)
P = a+b+c

print(f" Гипотенуза будет равна {c} \n Периметр будет равен {P}")