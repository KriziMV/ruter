shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part = input('Название детали: ')
cost = 0
coincidence = 0
all_parts = len(shop)

for ind in range(all_parts):  # loop to determine the index (цикл для определения индекса)
    if part.lower() == shop[ind][0]:  # Find the user-defined element (находим элемент заданный пользователем)
        coincidence += 1  # counting identical parts (подсчет одинаковых деталей)
        cost += shop[ind][1]  # we sum up the values of the second elements (суммируем значения вторых элементов)
print('Количество деталей: ', coincidence)
print('Общая стоимость: ', cost)
