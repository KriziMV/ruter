
text = input('Введите строку: ')

search = [ind for ind in range(len(text)) if text[ind] == 'h']  # a loop that finds the indexes of the characters you are looking for
                                                                # (цикл находящий индексы искомых символов)
segment = text[search[0] + 1:search[1]]  # make a slice between two characters (делаем срез между двух символов)

print('Развёрнутая последовательность между первым и последним h: ',
      segment[::-1])  # Unfold the sequence (разворачиваем последовательность)

