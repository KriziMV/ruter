
# Вариант 1:
# В данной задаче, если я сделаю в цикле for итерацию самих объектов списка, то мне придётся создавать ещё одну переменную для индексов, а при помощи ... range (len(...))
# я могу сразу задать нужные индексы в  самом цикле в соответствии с количеством элементов в списке, я если честно не совсем понял как я могу сократить код (либо его улучшить)
def sort():  # Selective sorting function (функция выборочной сортировки)
    for ind in range(len(first_list)):  # loop forming indexes according to the number of elements in the list
                                        # (цикл, образующий индексы в соответствии с количеством элементов в списке)
        minimum = ind
        for ind_2 in range(ind + 1,
                           len(first_list)):  # the same cycle, but after each iteration the index is shifted by one
                                              # (такой же цикл, но после каждой итерации индекс смещается на один)
            if first_list[ind_2] < first_list[minimum]:  # check two elements, with given indexes, for which of them is less than
                                                         # (проверка дух элементов, с заданными индексами, на то,какое из них меньше)
                minimum = ind_2  # fix the minimum to a smaller element (закрепляем минимум за меньшим элементом)

        first_list[minimum], first_list[ind] = first_list[ind], first_list[minimum]  # Assign a value to (перепресваеваем значения)

    print('Отсортированный список учеников:', first_list)


first_list = list(range(160, 176, 2))
second_list = list(range(163, 180, 3))
first_list.extend(second_list)  # merging two lists (объединение двух списков)

sort()

# Вариант 2:

first_list = list(range(160, 176, 2))
second_list = list(range(163, 180, 3))
first_list.extend(second_list)  # merging two lists (объединение двух списков)

print('Отсортированный список учеников:', sorted(first_list))  # output and sorting in ascending order (вывод и сортировка по возрастанию)
