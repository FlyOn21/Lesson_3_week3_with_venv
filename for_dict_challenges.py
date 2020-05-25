# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


def counter_name_in_dict(students):
    all_name = []
    dict_name = {}
    for name_dict in students:
        for name in name_dict.values():
            all_name.append(name)
    # print(all_name)
    set_name = set(all_name)
    # print(set_name)
    for name_in_set in set_name:
        count_name = all_name.count(name_in_set)
        dict_name[name_in_set] = count_name
    return dict_name


a = counter_name_in_dict(students)
print(a)

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students_1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_dic = counter_name_in_dict(students=students_1)
name_win = max(name_dic, key=lambda name: name_dic[name])
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
    nomber_class += 1
    name_dic_z2 = counter_name_in_dict(students=class_in)
    name_win_2 = max(name_dic_z2, key=lambda name: name_dic_z2[name])
    print(f'Самое частое имя в классе {nomber_class}:{name_win_2}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school_12 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male_1 = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


def count_boy_gerl(school_12, is_male_1):
    class_gender_count = []
    for class_school in school_12:
        num_class = class_school['class']
        students_in_class = class_school['students']
        class_dict = {}
        boy = 0
        gerl = 0
        for name_dic_3 in students_in_class:
            for name in name_dic_3.values():
                if is_male_1[name] is True:
                    boy += 1
                else:
                    gerl += 1
                class_dict['class'] = num_class
                class_dict['boy'] = boy
                class_dict['gerl'] = gerl
        class_gender_count.append(class_dict)
    return class_gender_count


c = count_boy_gerl(school_12, is_male_1)
print(c)

# for class_in_school in school:
#     class_name = class_in_school['class']
#     count_boy_gerl(school,is_male)
#     print(f'В классе {class_name} {gerl} девочки и {boy} мальчика')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school_13 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},{'first_name': 'Маша'}]},
    {'class': '5a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'},{'first_name': 'Маша'}]}

]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


dict_school = count_boy_gerl(school_12 = school_13,is_male_1 = is_male)
def find_max_class(dict_school):
    class_list = []
    boy_list = []
    gerl_list = []
    for school_class in dict_school:
        class_list.append(school_class['class'])
        boy_list.append(school_class['boy'])
        gerl_list.append(school_class['gerl'])

        boy_max_inclass = max(boy_list)
        find_index_name_class = boy_list.index(boy_max_inclass)
        find_class_boy = class_list[find_index_name_class]

        gerl_max_inclass = max(gerl_list)
        find_index_name_class = gerl_list.index(gerl_max_inclass)
        find_class_gerl = class_list[find_index_name_class]
    return (find_class_boy,find_class_gerl)

gender_class = find_max_class(dict_school)
print(f'Больше всего мальчиков в классе',gender_class[0])
print(f'Больше всего девочек в классе',gender_class[1])


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
