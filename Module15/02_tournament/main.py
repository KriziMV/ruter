
lisst = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = []
every_other = 0

for ind in lisst:
    every_other += 1  # Count each element (счетчик всех элементов)
    if every_other % 2 != 0:  # if divided with a remainder, then the index of the element is even
                             # (если делиться с остатком, то индекс у элемента четный)
        new_list.append(ind)  # Form a list of the necessary elements (формируем список из необходимых элементов)
print('Первый день: ', new_list)
