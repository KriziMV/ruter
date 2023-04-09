
lisst = []
number = int(input('Введите число: '))

for ind in range(number + 1):
    if ind % 2 != 0:  # we find the indices that divide by two with a remainder - these are our odd ones
                     # (находим индексы которые, делятся на два с остатком - это наши нечётные)
        lisst.append(ind)  # create a list of odd ones (создаем список из нечётных)
print('Список из нечётных чисел от одного до N: ', lisst)
