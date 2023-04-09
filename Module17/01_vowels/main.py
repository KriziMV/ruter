

text = input('Введите текст: ')
vowel_list = [letter for letter in text if letter in 'аиеёоуыэюя'] # Passing through a sentence in a loop with a vowel check
                                                                   # (прохождение по предложению циклом с проверкой на наличие гласных)

print('Список гласных букв: ', vowel_list,'\nДлина списка:', len(vowel_list))
