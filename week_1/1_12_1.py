# Напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона
# На вход программе подаются целые числа, выводом программы должно являться вещественное число, соответствующее площади треугольника.

a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
print ((p * (p - a) * (p - b) * (p - c)) ** 0.5)