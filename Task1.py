# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

from random import randint

m = 1
n = 10
List = list(set(randint(m, n) for i in range(1, 10)))
List.sort(reverse = True)
print(List)
