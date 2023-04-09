
def list_generator():  # The function generates lists that the user specifies
                       # (функция, генерирующая первые списки, задаваемые пользователем)
    first_lists = [int(input('Введите число: ')) for _ in range(3)] # Create a list of three items (создание списка из трех элементов)
    return first_lists
created_list = [list_generator() for _ in range(4)] # A loop that creates a list of values coming from the function
                                                    # (цикл который создает список приходящих из функции значений)

print(created_list)
