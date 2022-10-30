# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента.
# Use comprehension.

from random import randint

user_number = int(input('Сколько чисел в списке: '))

def f(x):
    x = randint(1, 30)
    return x

my_list = [f(i) for i in range(user_number)]
print(my_list)

new_list = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i] < my_list[i + 1]]
print(new_list)