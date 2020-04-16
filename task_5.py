################################################################################################
# TASK 5

my_rating_list = [1, 2, 3, 4, 5]
while True:
    try:
        user_input = int(input('Введите новый элемент "рейтинга"'))
        break
    except ValueError:
        print('Запрашиваемые данные необходимо ввести числом')

my_rating_list.append(user_input)
my_rating_list = sorted(my_rating_list)
print(my_rating_list)
while True:
    try:
        more_or_quit = int(input('Введите ещё один элемент или нажмите "ENTER" для завершения'))
    except ValueError:
        print('Всего хорошего :)')
        break
    else:
        my_rating_list.append(more_or_quit)
        my_rating_list = sorted(my_rating_list)
        print(my_rating_list)

#################################################################################################


