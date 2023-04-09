
def palindrome(num_list):  # a function that determines the palindromic nature of the numbers
                           # (функция которая определяет палиндромность чисел)
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1,-1):  # loop to go through the number in reverse order
                                                    # (цикл прохождения по числу в обратном порядке)
        reverse_list.append(num_list[i_num])  # list in reverse order (список в обратном порядке)
    if num_list == reverse_list:  # comparison of the incoming list with its reverse copy
                                   # (сравнение входячего списка с обратной его копией)
        return True
    else:
        return False


nums = [1, 7, 3, 4, 5, 4]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):  # transforming loop, which helps to select the desired indexes in the following loops
                                     # (преобразующий цикл, который помогает выбрать нужные индексы в следующих циклах)
    for ind in range(i_nums, len(nums)):  # cycle, which reduces the number of indexes by 1 with each iteration
                                          # (цикл который с каждей итерацией уменьшает количество индексов на 1)
        new_nums.append(nums[ind])  # create a list with one less element with each iteration of the first cycle
                                     # (создание списка, который с каждой итерацией первого цикла, будет на 1 элемент(первый) меньше)
    if palindrome(new_nums):  # check which part of the number is a palindrome (проверяем какая часть числа являеться палиндромом)
        for ind_2 in range(0, i_nums):  # if there is a match, the digit from the index of the first cycle where the match was found will be the final
                                         # (если палиндром, то цифра из индексов первого цикла, на которой нашли палиндром, будет концом)
            answer.append(nums[ind_2])  # Using indexes, we create a list of the missing part (с помощью индексов создаем список недостающей части)
        answer.reverse()  # Unfold the missing part (разворачиваем недостающую часть)
        break
    new_nums = []

print('Последовательность: ', nums)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)

