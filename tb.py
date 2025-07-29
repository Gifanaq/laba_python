

from collections import deque
from os import close


def next_power_of_two(n):
    if n <= 1:
        return 1
    return 1 << (n - 1).bit_length()


def build_segment_tree(arr):
    n = len(arr)
    size = next_power_of_two(n)

    # Дополняем массив нулями до степени двойки
    padded_arr = arr.copy()
    padded_arr.extend([0] * (size - n))


def recursion_building_tree (start,finish):
    if start == finish:
        return


class derevo_otrezkov:
    array = []
    def __init__(self,array):
        self.n = len(array)
        self.size = next_power_of_two(self.n)

        # Строим дерево отрезков
        self.array = [0] * (2 * self.size)

        # Заполняем листья
        for i in range(self.n):
            self.array[self.size + i] = array[i]

        # Строим остальные узлы
        for i in range(self.size - 1, 0, -1):
            self.array[i] = self.array[2 * i] + self.array[2 * i + 1]
        self.array = ["*"] + self.array
        # n = len(array)
        # size = next_power_of_two(n)
        # d = deque()
        #
        # # Дополняем массив нулями до степени двойки
        # padded_arr = array.copy()
        # padded_arr.extend([0] * (size - n))
        #
        # self.array += padded_arr
        #
        # array_for_work = []
        # for i in  self.array[::-1]:
        #     d.append(i)
        # while d:
        #     if len(d)==1:
        #         break
        #     else:
        #         a1 = d.popleft()
        #         a2 = d.popleft()
        #         res = a1 + a2
        #         self.array  =  [res] + self.array
        #         d.append(res)
        # self.array = ["*"] + self.array

    def suma_uchastok (self, start, finish, number_element = 1, isx = 1, kon = None):
        if kon is None:
            kon  =  len(self.array)//2 - 1
        # if number_element >
        # 1. Если текущий отрезок не пересекается с запросом
        if isx > finish or kon < start:
            return 0

            # 2. Если текущий отрезок полностью внутри запроса
        if start <= isx and kon <= finish:
            return self.array[number_element]
        return self.suma_uchastok(start, finish, number_element * 2, isx, (isx +kon) // 2) + self.suma_uchastok(start,
                                                                                                         finish,
                                                                                                         number_element * 2 + 1,
                                                                                                                ( isx +  kon )// 2 + 1,
                                                                                                         kon)

    def update(self, pos, value):
        pos += len(self.array)//2   - 1  # Переходим к листу
        self.array[pos] = value

        while pos > 1:
            pos >>= 1  # Идём к родителю
            new_val = self.array[2 * pos] + self.array[2 * pos + 1]
            if self.array[pos] == new_val:
                break  # Если сумма не изменилась, дальше можно не идти
            self.array[pos] = new_val

















# a = derevo_otrezkov([5,4,2,3,5])
# a.update(2,10)
# print(a.array)
# # print(a.suma_uchastok(2,5))
n,m = map(int,input().split())
ans = []
a = derevo_otrezkov(list(map(int,input().split())))
for i in range (m):
    g,p,c = map(int,input().split())
    if g==1:
        a.update(p + 1   ,c)
    elif g==2:
        ans.append(a.suma_uchastok(p +  1,c  ))
for i in ans:
    print(i)