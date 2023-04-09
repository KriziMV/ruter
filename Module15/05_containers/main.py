
quantity = int(input('Количество контейнеров: '))
list_cont = []

for _ in range(quantity):  # loop to create a list from the input data (цикл для создания списка из вводимых данных)
    weight = int(input('Введите вес контейнера: '))
    if weight < 200:  # set the maximum weight of the container (задаем максимальный вес контейнера)
        list_cont.append(weight) # If it fits the condition, then create a list (если подходит по условию, то создаем список)
    else:
        print('Вес контейнера слишком большой!')

new_weight = int(input('Введите вес нового контейнера: '))
cont_number = 0

for ind in list_cont:  # cycle to check all containers (цикл для перебора всех контейнеров)
    cont_number += 1  # count what number the container has (счетчик номера контейнера)
    if new_weight > ind:  # Find the position of the new container (находим позицию нового контейнера)
        print('Номер, который получит новый контейнер: ', cont_number)
        break
