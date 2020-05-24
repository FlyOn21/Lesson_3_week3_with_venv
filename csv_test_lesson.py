import csv
# with open(r'c:\Users\zhogo\PycharmProjects\Week_3\magento_ru.csv','r',encoding='utf-8') as file:
#     reader = csv.DictReader(file,delimiter = ',')
#     for line in file:
#         print(line)


# with open('magento_ru.csv','r',encoding='utf-8') as file:
#     reader = csv.DictReader(file,delimiter = '\n')
#     for line in file:
#         f = line.replace('\n','')
#         print(f)

list_for_csv =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
with open('list_for_csv.csv','w',encoding='utf-8') as export_file:
    filds = ['name', 'age','job']
    write_data = csv.DictWriter(export_file,filds, delimiter = ';')
    write_data.writeheader()
    for dict_to_write in list_for_csv:
        write_data.writerow(dict_to_write)


