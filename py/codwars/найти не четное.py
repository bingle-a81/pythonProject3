a=[11,160, 3, 1719, 19, 11, 13]

def find_outlier(integers):
    k0=[]
    k1=[]
    for i in range(len(integers)):
        if int(integers[i]) % 2 == 0:
            k0.append(integers[i])
        else:
            k1.append(integers[i])

    if len(k0)==1:
        return k0[0]
    if len(k1)==1:
        return k1[0]


print(find_outlier(a))