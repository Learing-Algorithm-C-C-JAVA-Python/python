# 伪代码:
# //基数排序算法，array 为待排序序列
# radixSort(array):
#     max = getMax(array)   // 查找 array 序列中的最大值
#     place <- 1            // 默认从个位开始排序
#     while max/place > 0 : // 将最大值的位数作为循环次数
#         countingSort(array, place)  // 调用计数排序算法，根据所选数位对各个元素进行排序
#         place = place * 10

# //计数排序算法，array 为待排序序列，place 指排序所依照的数位
# countingSort(array, place)
#     size <- len(array)       // 获取 array 序列中的元素个数
#     // 根据 place，找到相应数位值最大的元素
#     max <- (array[0] / place) % 10    
#     for i <- 1 to size:
#         if (array[i] / place) % 10 > max：
#             max <- array[i]
#     // 创建 count[max+1]，统计各个元素的出现次数
#     for j <- 0 to size     
#         count[(array[i] / place) % 10] <- count[(array[i] / place) % 10] + 1
#     // 对 count[max+1] 存储的元素做累加操作
#     for i <- 1 to max
#         count[i] <- count[i] + count[i - 1];
#     // 根据 count[max+1] 中的累加值，找到各个元素排序后的具体位置
#     for j <- size down to 0
#         output[count[(array[i] / place) % 10] - 1] <- array[i];
#         // 确定一个元素的位置后，count[max+1] 中相应位置的数值要减 1
#         count[(array[i] / place) % 10] <- count[(array[i] / place) % 10] - 1 
#     return output[size]
array = [121, 432, 564, 23, 1, 45, 788]
#计数排序算法，place 表示以指定数位为准，对序列中的元素进行排序
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    # 找到真正数位上值最大的元素
    max_element =  int(array[0] // place) % 10
    for i in range(1,size):
        if  (array[i] // place) % 10 > max_element:
            max_element = array[i]      
    #创建一个列表，统计各个元素的出现次数
    count = [0] * (max_element+1)
    for i in range(0, size):
        count[(array[i]//place) % 10] += 1
    #累加 count 数组中的出现次数
    for i in range(1, max_element):
        count[i] += count[i - 1]
    #根据 count 数组中的信息，找到各个元素排序后所在位置，存储在 output 数组中
    i = size - 1
    while i >= 0:
        output[count[(array[i]//place) % 10] - 1] = array[i]
        count[(array[i]//place) % 10] -= 1
        i -= 1
    #将 output 数组中的数据原封不动地拷贝到 array 数组中
    for i in range(0, size):
        array[i] = output[i]
# 基数排序算法
def radixSort(array):
    # 找到序列中的最大值
    max_element = max(array)
    # 根据最大值具有的位数，从低位依次调用计数排序算法
    place = 1
    while max_element//place :
        countingSort(array, place)
        place *= 10
radixSort(array)
print(array)
