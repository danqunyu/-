# 排序算法
# lowB 排序：冒泡排序，选择排序，插入排序
# NB 排序：快速排序，堆排序，归并排序
# 其他排序：希尔排序，计数排序，基数排序
import random


def bubble_sort(li):  # 每一趟排序，都会使得无序列表中的最大值往最上面走
    for i in range(len(li) - 1):  # 第i趟排序
        exchange = False
        for j in range(len(li) - i - 1):  # 在第i趟中，j代表当前箭头指向的数字，将判断第j个数是否比第j+1个数字大
            if li[j] > li[j + 1]:
                li[j + 1], li[j] = li[j], li[j + 1]
                exchange = True
        if not exchange:
            return li
    pass


def select_sort_simple(li):  # 不是原地排序，而且新生成li_new,需要多占一份内存
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li)-1): #i是第i趟对无序序列进行排序
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


    pass


def insert_sort(li):
    for i in range(1, len(li)): #手上已经有i张牌，再从无序序列中摸另外一张牌，进行插入排序。这张牌的index = i
        j = i-1
        tmp = li[i]
        while j>=0 and li[j] > tmp:
            li[j+1] = li[j]
            li[j] = tmp
            j -= 1
    pass


li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)

li = [random.randint(0, 100) for i in range(10)]
print(li)
select_sort(li)
print(li)


li = [random.randint(0, 100) for i in range(10)]
print(li)
insert_sort(li)
print(li)