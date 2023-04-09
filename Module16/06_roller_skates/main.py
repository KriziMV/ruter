
def lists(a, b):  # function that creates a list of given items (функция создающая список из заданных элементов)
    ready_list = []
    for ind in range(a):  # loop to create a new list (цикл для создания нового списка)
        print(f'Размер {b} {ind + 1}:', end='')
        user_input = int(input())
        ready_list.append(user_input)
    return ready_list


number_rollers = int(input('Кол-во коньков: ')) # number of rollers in the list (can be corrected to be set by the user) (количество роликов в списке (можно исправить чтобы задавал пользователь))
insert_1 = 'пары'
list_rollers = lists(number_rollers, insert_1)  # Creating a list of rollers  (создаем список из роликов)

number_sizes = int(input('\nКол-во людей: '))
insert_2 = 'ноги человека'
size_list = lists(number_sizes, insert_2)  # Creating a list with leg sizes (создание списка с размерами ног)

matching_size = []
people_with_roller = 0
flag = False

for foot in size_list:  # Foot size selection cycle (цикл для перебора размера ног)
    for roller in list_rollers:  # Cycle for selecting rollers (цикл для перебора роликов)
        if foot <= roller:  # a condition that finds the right rollers (условие которое находит нужные ролики)
            matching_size.append(roller)  # Create a list of appropriate rollers (создаем список из подходящих роликов)
            flag = True  # raise the flag when the condition is met (поднимим флаг если зашли в это условие)
    if flag:  # If the flag is raised, it means that we have found a suitable option.
              # (если флаг поднят значит нашли подходящий вариант)
        people_with_roller += 1  # number of matches (количество совпадений)
        list_rollers.remove(min(matching_size))  # remove the smallest result from the list of suitable rollers
                                                 # (удаляем наименьший результат из списка подходящих роликов)
    flag = False
    matching_size = []

print(f'Наибольшее количество людей, которые могут взять ролики: {people_with_roller}')


