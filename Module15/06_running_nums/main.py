
listt = [1, 2, 3, 4, 5]
quantity = len(listt)  # count the number of characters in the list (считаем количество символов в списке)
first_half = []  # first half of the list before the shift (первая половина списка до сдвига)
second_half = []  # The second half of the list after the shift (вторая половина списка после сдвига )
shift = int(input('Сдвиг: '))
ind = 0  # indexing variable (переменная для индексации)

for item in listt:  # loop through the elements of the list (цикл проходящий по элементам списка)
    ind += 1  # determine the index number (определяем номер индекса)
    if ind <= quantity - shift:  # we subtract the shift from the characters in the list,
                                 # compare it to the index, and if it is less than or equal, we create the first part of a new list
                                 # (от символов в списке отнимаем сдвиг, сравниваем с индексом, если он меньше либо равен, то создаем первую часть нового списка)
        first_half.append(item)  # fill in the first half of the list before the shift (заполняем первую половину списка до сдвига)
    else:
        second_half.append(item)  # the rest we move to the second half (остальные переносим во вторую половину)
second_half += first_half  # connect the right side to the left side (соеденяем правую часть с левой)
print('Изначальный список: ', listt)
print('Сдвинутый список: ', second_half)
