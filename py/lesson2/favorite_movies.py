#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
my_favorite_movies+=','
# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
i=i1=0
st=''
print()
for i in range(len(my_favorite_movies)):
    if my_favorite_movies[i] == ',' :
        st=st+my_favorite_movies[i1:i]
        i1 = i+1
    i = i + 1
print(st)






