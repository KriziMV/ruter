guest_list = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guest_list)} человек: {guest_list}')
    action = input('Гость пришел или ушел? ')
    guest_name = input('Имя гостя: ')
    if action == 'пришел' and len(guest_list) < 6:  # the condition if the guest came and there are seats on the list
                                                    # (условие, если гость пришел и есть места в списке)
        print(f'Привет, {guest_name}')
        guest_list.append(guest_name)  # add a guest to the list (добавляем гостя в список)
    elif action == 'пришел' and len(guest_list) >= 6: # condition if there are no seats (условие, если нету мест)
        print(f'Прости, {guest_name}, но мест нет.')
    elif action == 'ушел':  # The condition if the guest has left (условие, если гость ушел)
        guest_list.remove(guest_name)  # exclude from the list the one who left (удаляем из списка ушедшего)
        print(f'Пока, {guest_name}!')
    else:
        print('Не корректный ввод!')
        break
