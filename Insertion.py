list = [10, 14, 19, 27, 33, 35, 42, 44,]


def Insertion_sort():
    length = len(list)
    for i in range(1, length):
        insertion_elem = list[i]
        postion = i;
        while list[postion] > i and list[postion - 1] > insertion_elem:
            list[postion] = list[postion - 1]
            postion = postion - 1
        if postion != i:
            list[postion] = insertion_elem


Insertion_sort()

for i in list:
    print(i, end=" ")
