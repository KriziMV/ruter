nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

extended_list = [third_attachment for first_attachment in nice_list for second_attachment in first_attachment
                 for third_attachment in second_attachment]  # Unpack nested lists in loops (циклами распаковываем вложенные списки)
print(extended_list)

