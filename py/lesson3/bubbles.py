# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(200, 300)
radius=100
for _ in range(3):
    radius+=5
    sd.circle(point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bub(point,radius):
    for _ in range(3):
        radius += 5
        sd.circle(point,radius)

bub(point,radius)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
