##############################################################################
# TASK 4

user_input = input('Введите чере пробел Ваше имя, фамилию и отчество').split()
str_num = 0
additional_symbol = ") "
for words in user_input:
    str_num += 1
    print(str_num, additional_symbol, words)

###############################################################################


