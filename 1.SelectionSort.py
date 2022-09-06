# python的排序算法
#待排序序列
list = [14,33,27,10,35,19,42,44]

def selection_sort():
    length = len(list)
    for i in range(length-1):
        min = i
        for j in range(i+1,length):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i],list[min] = list[min],list[i]
selection_sort()

for i in list:
    print(i,end=" ")
