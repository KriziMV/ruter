
quantity = int(input('Количество видеокарт:'))
old_list = []
new_list = []
maximum = 0

for ind in range(quantity):  # loop to create a list of given items (цикл для создания списка заданных элементов)
    print('Видиокарта', ind + 1, ':', end='')
    p = int(input())
    old_list.append(p)
print('Старый список видеокарт: ', old_list)

for ind in old_list:  # loop to find the maximal element of the list (цикл для нахождения максимального элемента из списка)
    if ind > maximum:  # Check which index is greater (проверяем, какой индекс больше)
        maximum = ind  # the highest value is stored in a new variable (наибольшее значение сохраняем в новой переменной)

for ind in old_list:  # loop to create a list without a maximum number (цикл для создания списка без максимального числа)
    if maximum > ind:  # If the maximal number is greater than the index, then the index is added to the new list
        new_list.append(ind)  # (если максимальное число больше, чем индекс, то индек вносим в новый список)
print('Новый список видеокарт: ', new_list)

