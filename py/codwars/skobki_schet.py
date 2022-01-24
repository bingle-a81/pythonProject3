# -*- coding: utf-8 -*-
# Напишите функцию, которая принимает строку скобок и определяет,
# является ли порядок скобок допустимым. Функция должна
# возвращать true, если строка допустима и false если она недопустима.
a="("

def valid_parentheses(string):
    d=0
    k1=0
    k2=0
    for i in string:
        if i=='(':
            k1+=1
        elif i==')':
            k2+=1
        else:
            string=string.replace(i,'')

        d=k1-k2
        if d<0:
            return False
    if d==0:
        return True
    else:
        return False



print(valid_parentheses(a))