#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint 

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow=sites['Moscow']
london=sites['London']
paris=sites['Paris']

mos_lon=round(((moscow[0]-london[0])**2+(moscow[1]-london[1])**2)**0.5,4)
mos_par=round(((moscow[0]-paris[0])**2+(moscow[1]-paris[1])**2)**0.5,4)
lon_par=round(((london[0]-paris[0])**2+(london[1]-paris[1])**2)**0.5,4)

distances['Moscow']={}
distances['Moscow']['London']=mos_lon
distances['Moscow']['Paris']=mos_par

distances['London']={}
distances['London']['Moscow']=mos_lon
distances['London']['Paris']=lon_par

distances['Paris']={}
distances['Paris']['Moscow']=mos_par
distances['Paris']['London']=lon_par

pprint(distances)

print (distances['Moscow']['London'])