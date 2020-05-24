# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
vasa = 0
peter = 0
masha = 0
for name_dict in students:
    for name in name_dict.values():
        if name == 'Вася':
            vasa += 1
        elif name == 'Петя':
            peter += 1
        else:
            masha += 1
print(f'Вася: {vasa} \nМаша: {masha} \nПетя: {peter}')


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
vasa = 0
peter = 0
masha = 0
olga = 0
name_dic = {}
for name_dict in students:
    for name in name_dict.values():
        if name == 'Вася':
            vasa += 1
        elif name == 'Петя':
            peter += 1
        elif name == 'Оля':
            olga +=1
        else:
            masha += 1
name_dic['Вася'] = vasa
name_dic['Петя'] = peter
name_dic['Оля'] = olga
name_dic['Маша'] = masha
name_win = max(name_dic, key = lambda name: name_dic[name])
print(f'Самое частое имя среди учеников:{name_win}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

nomber_class = 0
for class_in in school_students:
    vasa = 0
    peter = 0
    masha = 0
    olga = 0
    nomber_class += 1
    name_dic_z2 = {}
    for name_dict_z2 in class_in:
        for name_2 in name_dict_z2.values():
            if name_2 == 'Вася':
                vasa += 1
            elif name_2 == 'Петя':
                peter += 1
            elif name_2 == 'Оля':
                olga += 1
            else:
                masha += 1
    name_dic_z2['Вася'] = vasa
    name_dic_z2['Петя'] = peter
    name_dic_z2['Оля'] = olga
    name_dic_z2['Маша'] = masha
    name_win_2 = max(name_dic_z2, key=lambda name: name_dic_z2[name])
    print(f'Самое частое имя в классе {nomber_class}:{name_win_2}')





# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
def count_boy_gerl(school,is_mail):
    boy = 0
    gerl = 0
    students_in_class = class_in_school['students']
    for name_dic_3 in students_in_class:
        for name in name_dic_3.values():
            if is_male[name] == False:
                boy += 1
            else:
                gerl += 1
    return gerl,boy


for class_in_school in school:
    class_name = class_in_school['class']
    count_boy_gerl(school,is_male)
    print(f'В классе {class_name} {gerl} девочки и {boy} мальчика')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},

]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
count = 0
count_class = []
class_name_all = []
for class_in_school in school:
    class_name = class_in_school['class']
    class_name_all.append(class_name)
# print(class_name_all)
while count<len(school):
    count +=1
    for class_in_school in school:
         boy = 0
         gerl = 0
         students_in_class = class_in_school['students']
         for name_dic_3 in students_in_class:
              for name in name_dic_3.values():
                   if is_male[name] == False:
                        boy+=1
                   else:
                        gerl+=1
         count_class.append(boy)
         count_class.append(gerl)
    # print(count_class)
    break
boy_in_class = []
gerl_in_class = []
for index_1,valeu in enumerate(count_class,1):
    if index_1%2!=0:
        boy_in_class.append(valeu)
    else:
        gerl_in_class.append(valeu)
# print(boy_in_class,gerl_in_class)

boy_max_inclass = max(boy_in_class)
find_index_name_class = boy_in_class.index(boy_max_inclass)
find_class = class_name_all[find_index_name_class]
print (f'Больше всего мальчиков в классе {find_class}')

gerl_max_inclass = max(gerl_in_class)
find_index_name_class = gerl_in_class.index(gerl_max_inclass)
find_class = class_name_all[find_index_name_class]
print (f'Больше всего девочек в классе {find_class}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a