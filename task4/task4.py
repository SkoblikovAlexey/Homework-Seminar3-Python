# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# dec_num = int(input("Введите десятичное число: "))
# result = bin(dec_num)
# print(result)
# print(f'Двоичное представление десятичного числа {dec_num} = {result}')

def convert_to_bin(num):
    result = ''   
    while num > 0:
        result = str(num % 2) + result    
        num = num // 2
    return  result


dec_num = int(input("Введите десятичное число: ")) 
bin_num = convert_to_bin(dec_num)
print(f'Двоичное представление десятичного числа {dec_num} = {bin_num}')
