# def baby_shark_lyrics():
#     lst=['Baby','Mommy','Daddy','Grandma','Grandpa']
#     song=[e for e in ]


lst=[e for e in range(1,10)]
print (lst)


print([e for e in range(1,10) ])



def summ(x):
    if x==0:
        return 0
    else:
        f=summ(x-1)
        f=f+x
        return f

print('rec=',summ(5))

def summ1(x):
    d=0
    while x>0:
        d=d+x
        x=x-1
    return d

print(summ1(5))    

