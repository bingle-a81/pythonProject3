# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)-1

mes=['yan','feb','mar','apr','may','jin','jil','avg','sep','okt','nov','des']
dni=[31,28,31,30,31,30,31,31,30,31,30,31]

mrn=dict(enumerate(zip(mes,dni)))
mon,days=mrn.get(month)[0],mrn.get(month)[1]
print('Вы ввели', mon)
print('month='+mon,'days='+str(days))
