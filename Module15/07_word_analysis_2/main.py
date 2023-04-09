
user_word = input('Введите слово: ')
counter = 0  # reverse index counter (счетчик обратных индексов)
flag = True

for letter in user_word:  # A loop to search for the letters of the word (цикл для перебора букв из слова)
    counter -= 1  # Counting in reverse order (подсчет в обратном порядке)
    if letter != user_word[counter]:  # If at least one letter is not equal, switch the flag (если хоть одна буква не равна, переключаем флаг)
        flag = False
if flag == True:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')