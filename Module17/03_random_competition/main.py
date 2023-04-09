
import random

first_list = [round(random.uniform(5, 10), 2) for _ in range(20)] # a loop generating a random list of fractional numbers from 5 to 10
                                                                  # (цикл генерирующий рандомный список дробных чисел от 5 до 10)
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]  # same generator (такой же генератор)
winners = [first_list[ind] if first_list[ind] > second_list[ind]
           else second_list[ind] for ind in range(20)]  # A loop that finds the largest value from two lists
                                                       # (цикл находящий наибольшее значение из двух списков)
print ('Первая команда: ', first_list)
print ('Вторая команда: ', second_list)
print ('Победители тура: ', winners)

