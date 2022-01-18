#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1,'bear')

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo=zoo+birds

# уберите слона
#  и выведите список на консоль

zoo.pop(3)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

def kletka(stro):
    if stro in zoo:
        print (f'клетка {stro} = ',str(zoo.index(stro)+1))
    else:
        print(f'{stro} такого нет')

kletka('lion')
kletka('lak')

