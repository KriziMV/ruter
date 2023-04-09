
number = int(input('Введите число: '))
processed_list = [ind % 5 if ind % 2 != 0 else 1 for ind in range(number)] # a loop with specified conditions
                                                                            # (цикл с определенными условиями)

print ('Результат: ', processed_list)
