# -*- coding: utf-8 -*-
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#список если север,то значение юг,запад--восток
a = ["NORTH", "SOUTH", "SOUTH","SOUTH", "EAST", "WEST", "NORTH", "WEST","NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
def dirReduc(plan):
    new_plan = [] # список новый
    for d in plan: #значение d в списке
        if new_plan and new_plan[-1] == opposite[d]:
            #если значение в нью план текущее и предыдущее ==. то удаляем запись
            new_plan.pop()
        else:
            new_plan.append(d) #или прибавляем
    return new_plan

print(dirReduc(a))





#Давным-давно, на пути через старый дикий горный запад,
# ... человеку дали указания, как пройти из одной точки в другую.
# Направления были "СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК". Ясно, что "СЕВЕР" и
# "ЮГ" противоположны, "ЗАПАД" и "ВОСТОК" тоже.


a =["NORTH", "WEST", "SOUTH", "EAST"]

def dirReduc(arr):
    p=''
    i=0
    while i < (len(arr)):
        d=arr[i]
        if arr[i]=="NORTH":
            if p=="SOUTH":
                arr.pop(i)
                arr.pop(i-1)
                i=0
                p = ''
            else:
                p=arr[i]
                i+=1
        elif arr[i]=="SOUTH":
            if p=="NORTH":
                arr.pop(i)
                arr.pop(i-1)
                i=0
                p = ''
            else:
                p=arr[i]
                i += 1
        elif arr[i]=="EAST":
            if p=="WEST":
                arr.pop(i)
                arr.pop(i-1)
                i=0
                p = ''
            else:
                p=arr[i]
                i += 1
        elif arr[i]=="WEST":
            if p=="EAST":
                arr.pop(i)
                arr.pop(i-1)
                i=0
                p = ''
            else:
                p=arr[i]
                i += 1
        elif arr[i] == ";":
            break
    return arr

print(dirReduc(a))
