# -*- coding: utf-8 -*-
import random

lst=random.randint(1,100)
lst = []
for i in range(0, 100):
    lst.append(random.randint(1, 1000))



lst.sort()

#lst=[15, 39, 55, 55, 67, 81, 83, 92, 99, 123, 130, 148, 165, 165, 176, 178, 179, 181, 181, 194, 196, 202, 221, 243, 248, 252, 253, 262, 278, 280, 281, 281, 292, 303, 310, 332, 335, 339, 339, 343, 358, 364, 373, 390, 394, 397, 406, 412, 427, 483, 490, 494, 500, 504, 513, 516, 518, 532, 539, 544, 573, 579, 587, 605, 608, 627, 640, 648, 649, 650, 652, 681, 690, 694, 729, 735, 741, 752, 775, 776, 784, 806, 837, 846, 847, 851, 857, 868, 875, 876, 888, 892, 897, 908, 914, 922, 923, 970, 976, 981]
#
# print(lst)

def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return str(mid)
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid - 1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)


naity = int(input('Веди число поиска :'))

x = binarysearch(lst, naity, 0, len(lst)-1)

if x is False:
    print('Item ', naity, ' Not Found')
else:
    print('Item ', naity, 'Found in List',x)
