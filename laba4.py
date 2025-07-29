import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
from matplotlib.ticker import FormatStrFormatter


with cbook.get_sample_data("C:/Users/Пользователь/Documents/pc/Laba_Pyt/Vladislav.jpg") as image_file:
    image =   plt.imread(image_file)#Получаем фотографию
fig, axs = plt.subplots( #Создаем с 6 областей (2x3) для размещения диаграмм, графиков и иллюстраций,
    nrows=2,       # Количество строк
    ncols=3,       # Количество столбцов
    figsize=(16, 12)  # Размер фигуры в дюймах (ширина, высота)
)
axs[0,0].imshow(image)
axs[0,0].set_title("Владислав Кашапов",fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal')#добавляем название «График», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль,

data = []
with open("data.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])#Cчитываем данные построчно
x = np.array(data[0])#Значения x для графика
y = np.array(data[4])#Значения y для графика,так как у меня 4 вариант
# 1. Проверка и очистка данных
mask = ~np.isnan(y)  # Маска для не-NaN значений
x_clean = x[mask]
y_clean = y[mask]
# 2. Сортировка по x (если нужно)
sort_idx = np.argsort(x_clean)
x_sorted = x_clean[sort_idx]
y_sorted = y_clean[sort_idx]
# 3. Построение графика с улучшенной заливкой
# Положительные значения
axs[0,1].fill_between(x_sorted, y_sorted,
                where=(y_sorted > 0),
                color="#1c25b0",
                interpolate=True)  # Добавляем интерполяцию

# Отрицательные значения
axs[0,1].fill_between(x_sorted, y_sorted,
                where=(y_sorted < 0),
                color="#FF0000",
                interpolate=True)
# axs[0,1].fill_between(x, y, where=np.array(y)>0, color="#1c25b0")#Положительные, отрицательные разного цвета, способ задания HEX
# axs[0,1].fill_between(x, y, where=np.array(y)<0, color=("#FF0000"))#Положительные, отрицательные разного цвета, способ задания HEX
axs[0,1].set_xlabel('Время', fontsize=13, fontfamily="Courier New",  rotation=25)  # Параметры оси Х: название «Время», размер шрифта 13, тип шрифта Courier New, поворот 25 градусов
axs[0,1].set_ylabel('Температура', fontsize=13, fontfamily="Courier New", rotation=25)# Параметры оси Y: название «Температура, размер шрифта 13, тип шрифта Courier New, поворот 25 градусов
axs[0,1].grid(True)#Накладываем сетку
axs[0,1].set_title('График',fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal') #добавляем название «График», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль,

sborka_for_bar = []
with open("fig8.txt") as f:
    for line in f:
        sborka_for_bar.append([float(x) for x in line.split()])#Cчитываем данные построчно
cur = sborka_for_bar[6]#Интверал беру на строке 2*4 - 1, 4 - мой номер варианта
x_bar = []
for i in range (int(cur[0]),int(cur[1]) + 1):
    x_bar.append(float(i))#Добавляем все числа из интверала [x1;x2], который мы получили в cur

y_bar = sborka_for_bar[7]#Значение на оси y это следующая  строка после интверала для x
axs[0,2].bar(x_bar, y_bar, color="green")#чертим столбчатую диаграмму с зелеными колонками
axs[0,2].grid(True)#Наносим сетку
arrowprops = dict(arrowstyle="->", color=('red')) #словарь с параметрами стрелки:цвет красный
axs[0,2].annotate(                      #установка параметров надписи:расположение стрелки, расположение текста, цвет текста зеленый,  тип шрифта Arial, размер шрифта 13, не жирный, не курсив,
    "Aннотация",
    xy=(123.0, 5.0),
    xytext=(123.0  - 1, 5.0 + 2),
    arrowprops=arrowprops,
    color="#008000",
    fontfamily ='Arial',
    fontsize=13,
    fontweight='normal',
    fontstyle='normal'
)
axs[0,2].set_facecolor("yellow") #установка цвета фона
axs[0,2].set_title('Диаграмма',fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal')#добавляем название «Диаграмма», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль

koef = np.poly([-1.65, -0.9, 1.3])
x_legend = np.arange(-2, 3, 0.5)


y1_legend = []
for val in x_legend:
    y1_legend.append(np.sin(4*val) - np.cos(3*val))#Вычисляем y1=sin(4) - cos(3*x)

# Вычисляем p(x)
p_x = np.polyval(koef, x_legend)

# Вычисляем y2 = 0.4 * p(x)
y_2_legend = 0.4 * p_x#y2=0.4*p(x)

font = {'family' : "Comic Sans MS",#Шрифт в легенде Comic Sans MS, цвет шрифта красный, размер шрифта 13, жирность  light, стиль normal,
        'weight' : 'light',
        'style':'normal',
        'size'   : '13',
        }
axs[1,0].plot(x_legend, y1_legend, linestyle='dashdot', color = 'blue', label='Graph y1')
axs[1,0].plot(x_legend, y_2_legend, linestyle='dotted',color ='orange', label='Graph y2')
axs[1,0].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
axs[1,0].set_xticks(x_legend) #Задаем фиксированные деления

axs[1,0].set_xticklabels(x_legend,rotation=60)#Поворот подписей деления оси OX
axs[1,0].legend(loc='best', prop=font,labelcolor='red')#Локализация:наилучшее расположение,цвет шрифта легенды текста красный
axs[1,0].set_title('Графики с легендой',fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal')#добавляем название «Графики с легендой», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль

N=300
# Добавляем небольшой случайный разброс по X для каждой группы
x_pareto = np.random.normal(-1, 0.05, size=N)  # Группа слева
x_normal = np.random.normal(0, 0.05, size=N)   # Группа в центре
x_uniform = np.random.normal(1, 0.05, size=N)  # Группа справа

y_ras = np.random.pareto(4,size=N)#Парето (α =4);
z_ras = np.random.normal(7,2,size=N)#нормальный (µ =7, o=2)
w_ras = np.random.uniform(-2,2,size=N)#равномерный (min=-2, max= 2)
axs[1,1].scatter(x_pareto,y_ras, color=(0/255,128/255,0/255), s=1)#Размер точек 1
axs[1,1].scatter(x_normal,z_ras, color='orange', s=2)#Размер точек 2
axs[1,1].scatter(x_uniform,w_ras, color='#0000FF', s=1)#Размер точек 1
axs[1,1].set_title('Диаграммы рассеяния',fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal')#добавляем название «Диаграммы рассеяния», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль


t = np.linspace(0, 100, 5000)
# axs[1,2].figure(figsize=(4,4))
axs[1,2].plot(3*np.sin(7.2 * t + np.pi/6), 9*np.cos(6 * t), color='red')#A = 3	B = 9	a = 7.2 b = 	6 сдвиг = 	π /6
axs[1,2].grid(color='gray')#цвет сетки серый
axs[1,2].set_title('График фигур Лиссажу',fontfamily="Comic Sans MS",color=('b',0.1),fontsize=15,fontweight='bold',fontstyle='normal')#добавляем название «График фигур Лиссажу», шрифт Comic Sans MS",синий цвет с прозрачностью 0.1,размер шрифта 15,жирный шрифт, обычный стиль

# plt.tight_layout()#Автоматическая настройка отступов
plt.show()#Показываем полученное
