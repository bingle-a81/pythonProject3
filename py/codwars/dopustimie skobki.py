# Напишите функцию, которая принимает строку фигурных скобок и определяет,
# является ли порядок фигурных скобок допустимым. Он должен вернутьсяtrue,
# если строка допустима и falseесли она недопустима.
# Все входные строки будут непустыми и будут состоять только из круглых скобок, скобок и 
# фигурных скобок: ()[]{}.
# Что считается действительным?
# Строка фигурных скобок считается допустимой, если все фигурные скобки соответствуют правильной
#  фигурной скобке.
# Примеры
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False
a="[({})](]"


def validBraces(string):
    k1 = string.find("{")
    k2 = string.find('}')
    if k1 < 0 or k2 < k1 or k2 - k1 == 1:
        return False
    else:
        return True


print(validBraces(a))


def validBraces(string):
    lst=list(string)
    ww=0

    list1=[]

    for r in range(len(lst)):

        if lst[r]=='{':
            list1.append(1)
        elif lst[r]=='}':
            list1.append(-1)

    if len((list1))==0:
        return False
    else:
        for k in range(len(list1)):
            ww+=list1[k]
            if ww<0:
                return False
        if ww==0:
            return True
        else:
            return False