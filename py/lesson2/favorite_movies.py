# работа со строками и словарями!

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
my_favorite_movies+=','

i=i1=0#индексы для разбора строки
st=''#пустая строка
dict1={}#пустой словарь
nom_slovara=0 #индекс ключей словаря

for i in range(len(my_favorite_movies)):
    if my_favorite_movies[i] == ',' :
        st=st+my_favorite_movies[i1:i]
        nom_slovara+=1
        dict1['key'+str(nom_slovara)]=my_favorite_movies[i1:i]
        i1 =i+1

    i += 1
print(st)
print(dict1['key1'],dict1['key'+str(nom_slovara)],dict1['key2'],dict1['key'+str(nom_slovara-1)])





