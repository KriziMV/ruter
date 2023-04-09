violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

amount_minutes = 0
total_songs = int(input('Сколько песен выбрать?: '))

for counting in range(total_songs):  # loop to enter songs (цикл для ввода песен)
    print(f'Название {counting + 1}-й песни: ', end='')
    user_song = input()
    for ind in range(len(violator_songs)):  # loop to find the desired song and summarize the minutes
                                            # (цикл для нахождения нужнойпесни и суммирования минут)
        if user_song == violator_songs[ind][0]:  # Find the user-defined element(находим элемент заданный пользователем)
            amount_minutes += violator_songs[ind][1]  # we sum up the values of the second elements
                                                     # (суммируем значения вторых элементов)

print(f'Общее время звучания песен — {round(amount_minutes, 2)} минуты')

