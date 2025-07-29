# sborka_for_bar = []
# with open("fig8.txt") as f:
#     for line in f:
#         sborka_for_bar.append([float(x) for x in line.split()])#Cчитываем данные построчно
# cur = sborka_for_bar[6]
# x_bar = []
# for i in range (int(cur[0]),int(cur[1]) + 1):
#     x_bar.append(float(i))
#
# y_bar = sborka_for_bar[7]
# print(x_bar)
# print(y_bar)
import numpy as np
koef = np.poly([-1, 1.5, 2])
x = np.arange(-2, 2.1, 0.5)
y1 = []
for val in x:
    print(val)
    y1.append(np.sin(3*val) + np.sin(2*val+np.pi))

