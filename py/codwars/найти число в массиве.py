# -*- coding: utf-8 -*-
#=========================================
# Учитывая массив целых чисел, найдите то, которое появляется нечетное число раз.
#
# Всегда будет только одно целое число, которое появляется нечетное число раз.
#
# Примеры
# [7] должен вернуться 7, потому что это происходит 1 раз (что странно).
# [0] должен вернуться 0, потому что это происходит 1 раз (что странно).
# [1,1,2] должен вернуться 2, потому что это происходит 1 раз (что странно).
# [0,1,0,1,0] должен вернуться 0, потому что это происходит 3 раза (что странно).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] должен вернуться 4
#================================================

from itertools import groupby


lst=[5,4,3,2,1,5,4,3,2,10,10]

print(lst)


def find_it(seq):
    seq.sort()
    for k, g in groupby(seq.sort()):
        if len(list(g)) % 2 != 0:
            return k

print(find_it(lst))

