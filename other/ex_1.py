"""
Необходимо в массиве найти повторяющиеся значения, если такие найдены, вернуть-True, иначе-False
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""

# if __name__ == '__main__':
#     nums = [1, 2, 3, 1]
#     print(len(nums)!=len(set(nums)))
#     nums = [1,2,3,4]
#     print(len(nums) != len(set(nums)))

"""
Имеется 2 массива, один содержит название, второй значения необходимо получить значение score_2, если score_2 - нет, то значение будет 0.23241
Input:
names = ['score_1', 'score_2', 'score_3']
values = [0.2323, 0.12131, 1.2241]
Output: 0.12131

Input:
names = ['score_1', 'score_3', 'score_4']
values = [0.2323, 0.12131, 1.2241]
Output: 0.23241
"""

# if __name__ == '__main__':
#     names = ['score_1', 'score_3', 'score_4']
#     values = [0.2323, 0.12131, 1.2241]
#     for name, val in zip(names, values):
#         if name == 'score_2':
#             print(val)
#     else:
#         print(0.23241)

"""
Реализуйте функцию custom_filter(), которая на вход принимает список some_list, с любыми типами данных,
находит в этом списке целые числа, отбирает из них те, что делятся нацело на 7,
суммирует их, а затем проверяет превышает эта сумма 83 или нет. Если НЕ превышает - функция должна вернуть True, если превышает - False.
Input: some_list = [7, 14, 28, 32, 32, 56]
Output: False

Input: some_list = [7, 14, 28, 32, 32, '56']
Output: True
"""


def custom_filter(some_list):
    s = 0
    for el in some_list:
        if isinstance(el, int) and el % 7 == 0:
            s += el
            if s > 83:
                return False
    return True


if __name__ == '__main__':
    print(custom_filter([7, 14, 28, 32, 32, 56]))
    print(custom_filter([7, 14, 28, 32, 32, '56']))
