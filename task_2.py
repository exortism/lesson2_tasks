###########################################################################
# TASK 2

my_list = []
element_1 = input("Введите Ваше имя")
element_2 = input("Введите Вашу фамилию")
element_3 = input("Введите ваш возрасть")
element_4 = input("Введите город, в котором проживаете")
element_5 = input('Введите язык программирования, который вам интересен')
my_list.extend([element_1, element_2, element_3, element_4, element_5])
print(my_list)
my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]
print(my_list)

###########################################################################


