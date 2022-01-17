a=[160, 3, 1719, 19, 11, 13, -21]
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
                return (integers[i])
        else:
            if p==1:
                p=1
            else:
                return (integers[i])

print(find_outlier(a))