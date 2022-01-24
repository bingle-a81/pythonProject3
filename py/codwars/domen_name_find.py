# -*- coding: utf-8 -*-
# Напишите функцию, которая при задании URL-адреса в виде строки анализирует
# только доменное имя и возвращает его в виде строки.
#////////////////////////////////////////
#лучшее решение
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]
#////////////////////////////////////////

urrl="http://google.com"

ud=['http://','www.','https://']
def domain_name(urzl):
    for i in ud:
        if urzl.find(i)!=-1:
            urzl=urzl.replace(i,'')
    return urzl.split('.')[0]




print(domain_name(urrl))


