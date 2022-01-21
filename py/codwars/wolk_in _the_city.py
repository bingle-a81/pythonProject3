# wlk = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
#
#
# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     else:
#         north = walk.count('n')
#         south = walk.count('s')
#         east = walk.count('e')
#         west = walk.count('w')
#         if north == south and east == west:
#             return True
#         else:
#             return False
#
#     # determine if walk is valid
#     # pass
#
#
# print(is_valid_walk(wlk))


#Давным-давно, на пути через старый дикий горный запад,
# ... человеку дали указания, как пройти из одной точки в другую.
# Направления были "СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК". Ясно, что "СЕВЕР" и
# "ЮГ" противоположны, "ЗАПАД" и "ВОСТОК" тоже.
a =['NORTH', 'WEST', 'SOUTH', 'EAST']

def dirReduc(arr):
    north = arr.count("NORTH")
    south = arr.count("SOUTH")
    east = arr.count("EAST")
    west = arr.count("WEST")
    print(north,south,east,west)
    n_s=north-south
    e_w=east-west
    lst=[]
    if n_s==0 and e_w==0:
        lst=['NORTH', 'WEST', 'SOUTH', 'EAST']
    else:
        if n_s>0:
            while n_s>0:
                lst.append("NORTH")
                n_s-=1
        elif n_s<0:
            while i > n_s*(-1):
                lst.append("SOUTH")
                i += 1
        else:
            pass
        if e_w>0:
            while e_w>0:
                lst.append("EAST")
                e_w -= 1
        elif e_w<0:
            while e_w*(-1)>0:
                lst.append("WEST")
                e_w+= 1
        else:
            pass

    return lst

print(dirReduc(a))




