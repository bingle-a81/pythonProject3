# -*- coding: utf-8 -*-
import imp
from random import random
import simple_draw as sd

sd.resolution = (1200, 600)

# # Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(200, 300)
# radius=100
# for _ in range(3):
#     radius+=5
#     sd.circle(point, radius=radius)

# # Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bub(point,radius):
#     for _ in range(3):
#         radius += 5
#         sd.circle(point,radius)

# bub(point,radius)

# x=100
# for i in range(10):
#     x+=100
#     point = sd.get_point(x, 200)
#     sd.circle(point,radius)

# for x1 in range(200,1200,100):
#     point = sd.get_point(x1, 400)
#     sd.circle(point,radius)   


# # Нарисовать три ряда по 10 пузырьков
# for y in range(50,500,100):
#     for x3 in range(50,1200,100):
#         point = sd.get_point(x3, y)
#         sd.circle(point,radius)  



# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
import random
for _ in range(300):
    point=sd.random_point()
    color=sd.random_color()
    step=random.randint(2,5)

    sd.circle(point,color=color,width=step)


sd.pause()
