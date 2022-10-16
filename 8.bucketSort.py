#桶排序算法，array 为待排序序列
def bucketSort(array):
    bucket = []
    # 创建空桶
    for i in range(len(array)):
        bucket.append([])
    # 根据规则将所有元素分散到各个桶中
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # 分别对各个桶进行排序
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # 合并所有桶内的元素
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
array = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucketSort(array))
