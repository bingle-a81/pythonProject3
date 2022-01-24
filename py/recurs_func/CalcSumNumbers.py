#осуществляет суммирование чисел во входящем списке

import re
#
#
# def CalcSumNumbers(A):
#     if A == []:
#         # если набор пуст, возвратить 0
#         return 0
#     else:
#         # Вычислить сумму - прибавить первый элемент набора
#         summ = CalcSumNumbers(A[1:]) # рекурсивный вызов этой же функции
#
#         # Прибавить к общей сумме первый элемент
#         summ = summ + A[0]
#
#         return summ

# Демонстрация использования функции CalcSumNumbers()
# 1. Создать набор чисел
# L = [ 2, 3, 8, 11, 4, 6 ]
#
# # 2. Вызвать функцию
# summ = CalcSumNumbers(L)

# 3. Распечатать сумму
# print("summ = ", summ)

k=["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(k)

def summ_v_spiske(lst):
    if lst==[]:
        return 0
    else:
        su=summ_v_spiske(lst[1:])
        print(lst)
        su=su+lst[0]
        return su

print (summ_v_spiske(k))


