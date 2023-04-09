list_films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

quantity = int(input('Сколько фильмов хотите добавить?'))
favorite_mov = []
flag = False  # flag that determines whether the movie is in the list (флаг, определяющий наличие фильма в списке)
for _ in range(quantity): # loop to enter the number of user movies (цикл для ввода количества фильмов пользователя)
    print('Введите название фильма: ', end='')
    my_film = input()
    flag = False # each iteration we set the flag to "false". (каждую итерацию флаг ставим в положение - ложь)
    for films in list_films: # loop to go through the list of movies (цикл для перебора списка с фильмами)
        if films.lower() == my_film.lower(): # the condition determining the availability of the film (условие, определяющее наличие фильма)
            flag = True  # If the movie is on the list, move the flag to the position - true
                         # (если фильм в списке, переводим флаг в положение - правда)
            favorite_mov.append(my_film)
    if flag == False:  # if the flag remains in the position - false, there will be another condition
                       # (если флаг остался в положении - ложь, то будет другое условие)
        print(f'Ошибка: фильма {my_film} у нас нет :(')

print('Ваш список любимых фильмов: ', favorite_mov)
