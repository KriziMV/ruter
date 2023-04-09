a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)

# ниже мой вариант кода

def delete(a, b):  # function to remove unwanted items (функция для удаления не нужных элементов)
    lisst = []  # a new list to be filled with new items (новый список для заполнения новыми элементами)
    for ind in a:  # loop to try all elements (цикл для перебора всех элементов)
        if ind != b:  # the condition defining the unnecessary element (условие, определяющее ненужный элемент)
            lisst.append(ind)  # Combining all indexes into a list (объеденение всех индексов в список)
    return lisst


main_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]
unnecessary = 5  # Unnecessary item (лишний элемент)

main_list.extend(second_list)  # merge the two lists into one (объеденяем два списка в один)
finding_5 = main_list.count(5)  # counting fives in the lists (подсчет пятерок в "двух" списках)
main_list = delete(main_list,
                   unnecessary)  # returns the value from the function, with deleted elements (вернули значение из функции,
                                 # с удаленными элементами)

print(f'Количество цифр 5 при первом объединении: {finding_5}')

main_list.extend(third_list)  # Inserted a third list (вставили третий список)
finding_3 = main_list.count(3)  # counting threes in the overall list (подсчет троек в общем списке)

print(f'Количество цифр 3 при втором объединении: {finding_3}\nИтоговый список:{main_list}')

