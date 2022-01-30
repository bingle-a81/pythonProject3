# 1) все компсы и генэксп работают по принципу
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# читается это слева направо, что важно когда циклов больше 1.
# 2) принцип работы операций у листкомпс и генэксп одинаков, синтаксически различаются скобками
# 3) компсы (листкомпс, сеткомпс, дикткомпс) в результате своей работы формируют соответствующую 
# коллекцию и занимают память
# 4) переменные созданные внутри компсов или генэкспа недоступны извне
# 5) генэксп вернет объект, а не коллекцию! при создании объекта он проверит источник,
#  что может быть критично, если это какая то функция. Если источник не валидный то ошибка упадет 
#  при создании генератора, а не при попытке получить значение
# 6) генэксп ленивый, то есть ничего не делает и не занимает память пока не потребуется значение. 
# Сгенерировав значение снова засыпает пока опять не попросят новое.
# 7) генэксп одноразовый, при исчерпании начинает бросать исключение, которое мы не увидим, если 
# используем генератор в цикле for
# 8) генэксп может потенциально генерировать бесконечные последовательности, но он ничего не знает 
# о порядке элементов или о их количестве (нет len)


import pprint



squares=[e for e in range(10) if e%2==0]# все четные числа до 10

squares=([e**2 for e in range(10) if e%2==0])# ониже в квадрате

text='hello world my freands'
words=[x.capitalize() for x in text.split()]# разбить строку на слова и первая буква большая!


ints=[-1,-9,-8,9,-7]
positivs = [e for e in ints if e>0]

letters=[letter for word in text.split() for letter in word if letter>'m']
uniq_letters={letter for word in text.split() for letter in word if letter>'m'}#множества-списки уникальных объектов

matrix=[list(range(x,x+3)) for x in range(3)]

alfabet={index:letter for index,letter in enumerate('abcdefghjklmnop',1)}
change_alfabet={value:key for key,value in alfabet.items()}

# ===========================================
positivs_gen = (e for e in ints if e>0)

even_namb=(e for e in range(100) if e%2==0)



if __name__=='__main__':
    # print(squares)
    # print(words)
    # print(positivs)
    # print(letters)
    # print(uniq_letters)
    # pprint.pprint(matrix,indent=1,width=15)
    # print(alfabet)
    # print(change_alfabet)

    # ------------------------
    # print(positivs_gen)
    # print(next(positivs_gen))
    print(next(even_namb))
    print(next(even_namb))
    for i in even_namb:
        print(i)

