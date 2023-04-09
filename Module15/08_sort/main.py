
def sorted_list(lisst):  # function to sort the list (функция для сортировки списка)
    for ind in range(
            len(lisst)):  # count how many characters are in the list, and, using a loop, take each index to check in the next loop (подсчитать, сколько символов в списке, и, используя цикл, взять каждый индекс для проверки в следующем цикле)
        for i in range(ind,
                       len(lisst)):  # In this loop, we run through all the items in the list for comparison (в этом цикле прогоняем по всем элементам из списка, для сравнения)
            if lisst[i] < lisst[
                ind]:  # if the list with the index from the first cycle is bigger than the list with the index from the second cycle (если список с индексом из первого цикла, больше списка с индексом из второго цикла,... )
                lisst[i], lisst[ind] = lisst[ind], lisst[i]  # swap them around (...то меняем их местами)


lisst = [1, 4, -3, 0, 10]

sorted_list(lisst)

print(lisst)
