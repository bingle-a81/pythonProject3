a=1000

def zeros(n):
    chisl=0
    stepen=1
    kvadrat_5=0
    summa_noli=0
    while kvadrat_5<n:
        kvadrat_5=5**stepen
        chisl=n//kvadrat_5
        print(chisl)
        stepen+=1
        summa_noli+=chisl

    return summa_noli

print(zeros(a))