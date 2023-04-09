
start = 0
people = int(input('Количество человек: '))
counting = int(input('Какое число в считалке? '))
print(f'Значит,выбывает каждый {counting}-й человек')
list_people = list(range(1, people + 1))
stop = (start + counting - 1) % len(list_people)

while len(list_people) > 1:  # iterate until there is one item left in the list
                             # (итерируем пока не останеться один элемент в списке)
    print('\nТекущий круг людей:', list_people)
    print('Начало счёта с номера ', list_people[start])
    print('Выбывает человек под номером', list_people[stop])
    list_people.remove(list_people[stop])  # remove the element using the index of the element where the count ended
                                           # (удаляем элемент, используя индекс элемента на котором закончился счет )

    if len(list_people) > stop:  # As long as the list of people is larger than the size of the stop, we will not go beyond
                                 # (пока списак больше чем стоп, за рамки мы не выйдем)
        start = stop  # take the stop index as a start (берем за старт индекс стопа)
    else:
        start -= 1  # As soon as the number of people is less than (or equal to) the indexes do not fit, we subtract one index for correct counting
                    # (как только списак стал меньше (либо равен), индексы не влазят, отнимаем один индекс для корректного подсчета)
    stop = (start + counting - 1) % len(list_people)  # Finding a place to stop (вычесляем значение стопа)

print('Остался человек под номером ', list_people[0])
