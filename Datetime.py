from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'Ru-ru')

print(datetime.now().strftime('%a %d/%m/%g %H:%m'))

time_2 = '21/05/1986 02:00'
time_open = datetime.strptime(time_2,'%d/%m/%Y %H:%m')
print(time_open)