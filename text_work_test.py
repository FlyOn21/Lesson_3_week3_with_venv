def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_read:
        all_file = file_read.read()
        len_file_str = len(all_file)
        file_ch = all_file.replace('.', '!')
        file_count = file_ch.split()
        with open('referat_2.txt', 'w', encoding='utf-8') as ref_2:
            ref_2.write(file_ch)
        with open('referat_2.txt', 'a', encoding='utf-8') as ref_2:
            ref_2.write(f'\nКоличество слов в тексте {len(file_count)}  ')
        with open('referat_2.txt', 'a', encoding='utf-8') as ref_2:
            ref_2.write(f'Длинна строки {len_file_str}')

read_file('referat.txt')
