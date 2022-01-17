a=[11,2, 4, 0, 100, 4, 11, 2602, 36]
def find_outlier(integers):
    k=0
    if int(integers[0]) % 2 == 0:
        p = 0
    else:
        p=1
    for i in range(1,len(integers)):
        if int(integers[i])%2==0:
            if p==0:
                p=0
            else:
                k=integers[i]
        else:
            if p==1:
                p=1
            else:
                k = integers[i]


    return k

print(find_outlier(a))