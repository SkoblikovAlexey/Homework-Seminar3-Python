# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num_n = int(input("Введите количество чисел Фибоначчи: "))
list_num = []
temp = 0
count = 0
for i in range(0, num_n + 1):
    list_num.append(temp)
    if temp == 0:
        temp = 1
    temp += list_num[i - 1]
negative_list = []
count = len(list_num) - 1

for i in range(len(list_num)):
    if list_num[i] != 0 and i % 2 == 0:
        negative_list.append(list_num[i] * - 1)
    elif i % 2 != 0:
        negative_list.append(list_num[i])
negative_list = negative_list[::-1]
# list_merged = negative_list + list_num
negative_list.extend(list_num)
print(negative_list)
