#a = ['a', 'b', 'c', 4, (3, 2, 1)]
#b, c, d, e, g = a
#print(g)

# Распаковка элементов из последовательностей произвольной длинны
#def drop_first_lsat(grades):
#    first, *middle, last = grades
#    return middle
#pip = [1, 2, 3, 4, 5, 6]
#print(drop_first_lsat(pip))

# Оставляем N последних элементов
#from collections import deque
#def search(lines, pattern, history=5):
#    previos_lines = deque(maxlen=history)
#    for line in lines:
#        if pattern in line:
#            yield line, previos_lines
#        previos_lines.append(line)
#
#if __name__ == '__main__':
#    with open('struct_data_and_algoritm.py') as f:
#        for line, prevlines in search(f, 'python', 5):
#            for pline in prevlines:
#                print(pline, end='')
#            print(line, end='')
#            print('-'*20)

# Поиск N максимальных и минимальных элементов
#import heapq
#nums = [1, 2, 3, 4, 5, 6, 7, 10]
#print(heapq.nlargest(3, nums))
#print(heapq.nsmallest(3, nums))

# Реализация очереди с приоритетом
#import heapq
#class PriorityQueue:
#    def __init__(self):
#        self._queue = []
#        self._index = 0
#
#    def push(self, item, priotity):
#        heapq.heappush(self._queue, (-priotity, self._index, item))
#        self._index += 1
#
#    def pop(self):
#        return heapq.heappop(self._queue)[-1]

# Лучшая реализация создания словаря и заполнения через for
#from collections import defaultdict
#d = defaultdict(list)
#for key, value in pairs:
#    d[key].append(value)

# Поддержка порядка в словаре, для большиех проэктов
#from collections import OrderDict
#d = OrderdDict()

# Сортировка списка словарей по общему ключу. Может помочь с сортировкой в HH
#rows = [
#        {'sss': 'ssswe', 'b': 'bbb',}
#]
#from operator import itemgetter
#rows_by_fname = sorted(rows, key=itemgetter('sss')) # Сортировка по sss
#rows_by_uid = sorted(rows, key=itemgetter('b')) # Сортировка по ключу b
##можно передовать несколько ключей
#rows_by_lfname = sorted(rows, key=itemgetter('sss', 'b'))
## также можно указать min или max
#rows_by_min = min(rows, key=itemgetter('sss'))

#Группирование записей на основе полей. Может помочь в сортировке по дате в сериалах, отображать последние
rows = [
        {'adress': '5412 N CLARK', 'date': '07/01/2012'},
        # ...
]
from operator import itemgetter
from itertools import groupby
#Сначала сортируем по нужным полям
rows.sort(key=itemgetter('date'))
#Итерируем в группах
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
