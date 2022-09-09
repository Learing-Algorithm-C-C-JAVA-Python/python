#待排序序列
list = [35,33,42,10,14,19,27,44]
def shell_sort():
    length = len(list)
    # 初始化间隔数为 1
    interval = 1
    # 计算最大间隔
    while interval < (int)(length / 3):
        interval = interval * 3 + 1
    # 根据间隔数，不断划分序列，并对各子序列排序
    while interval > 0:
        # 对各个子序列做直接插入排序
        for i in range(interval , length):
            temp = list[i]
            j = i
            while j > interval - 1 and list[j - interval] >= temp:
                list[j] = list[j - interval]
                j = j - interval
            if j != i:
                list[j] = temp
        # 计算新的间隔数，继续划分序列
        interval = (int)((interval - 1)/3)
# 对待排序序列做希尔排序
shell_sort()
# 输出已排好序的序列
for i in list:
    print(i,end=" ")
