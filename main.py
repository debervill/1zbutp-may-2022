from tkinter.ttk import LabeledScale
from turtle import clear
import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
import csv 

with open('gruz-per.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    rows = list(csv_reader)

years = rows[4][1:len(rows[4])]
all_data = rows[7]

cl_data =all_data[1:len(all_data)]

clear_data = []

for i in range(len(cl_data)):
    if (cl_data[i].find(',') > -1):
        clear_data.append(float(cl_data[i].replace(',','.')))
    else:
        clear_data.append(float(cl_data[i]))



x = np.arange(len(clear_data))
width = 0.35

fig, ax = plt.subplots(figsize=(15,4), layout='constrained')

ax.set_ylabel('Перевезено (млн. т)')
ax.set_title('Годы')
ax.set_xticks(x)
ax.set_xticklabels(years)

pps = ax.bar(x - width/2, clear_data, width, label='population')
for p in pps:
   height = p.get_height()
   ax.annotate('{}'.format(height),
      xy=(p.get_x() + p.get_width() / 2, height),
      xytext=(0, 3), #Вертикальный отступ от столбца диаграммы до текста 
      textcoords="offset points",
      ha='center', va='bottom')

plt.show()