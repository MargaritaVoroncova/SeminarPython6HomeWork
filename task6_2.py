# 2. Для чисел в пределах 
# от 20 до N найти числа, кратные 20 или 21.
# Use comprehension.

user_number = int(input('Сколько чисел в списке: '))

my_list = [i for i in range(20, user_number + 1)]
print(my_list)
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] % 20 == 0 or my_list[i] % 21 == 0]
print(new_list)