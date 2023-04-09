
def encryption(text, offset):  # text encryption function (функция шифрования текста)
    list_signs = [(alphabet[(alphabet.index(i) + offset) % 33]
                   if i != ' ' else ' ') for i in text]  # loop with conditions, encrypt text (цикл с условиями, шифруем текст)
    return ''.join(list_signs)  # translate list to text (перевод списка в текст)

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_text = input('Введите сообщение: ')
set_offset = int(input('Введите сдвиг: '))

cipher = encryption(user_text, set_offset)

print ('Зашифрованный текст: ', cipher)

