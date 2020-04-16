########################################################################################################
# TASK 3 (by list)

year_list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
while True:
    try:
        user_input = int(input('Введите числом порядковый номер месяца (метод список)'))
        break
    except ValueError:
        print('Запрашиваемые данные необходимо ввести числом')

if user_input in year_list[0]:
    print('Это зима!')
elif user_input in year_list[1]:
    print('Это весна!')
elif user_input in year_list[2]:
    print('Это лето!')
else:
    print('Это осень!')

#########################################################################################################
# TASK 3 (by dict)

year_dict = dict({'Winter': [1, 2, 12], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11], 'Spring': [3, 4, 5]})
while True:
    try:
        user_input = int(input('Введите числом порядковый номер месяца (метод словарь)'))
        break
    except ValueError:
        print('Запрашиваемые данные необходимо ввести числом')

if user_input in year_dict['Winter']:
    print('Это зима!')
elif user_input in year_dict['Spring']:
    print('Это весна!')
elif user_input in year_dict['Summer']:
    print('Это лето!')
else:
    print('Это осень!')

#########################################################################################################


