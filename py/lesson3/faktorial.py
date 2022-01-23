def faktorial(chislo):
    if chislo==1:
        return 1
    faktorial_minus_1=faktorial(chislo-1)
    return chislo*faktorial_minus_1

print(faktorial(9))

