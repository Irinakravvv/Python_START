
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Результат округлить до сотых.

#Ввод: четыре значения типа <int>
#Вывод: значение типа <float>
#Пример:
#4 10
#11 5
#39.22

x1 = int(input("Введите первую кординат х"))
y1 = int(input("Введите первую кординат у"))
x2 = int(input("Введите  точку кординат x"))
y2 = int(input("Введите точку кординат у"))

n = ((x1 - x2)**2 + (y1-y2)**2) ** 0.5
print (n)