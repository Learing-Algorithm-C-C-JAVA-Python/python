# // 输入 arr[n]                                // 输入要排序的序列
# // merge_sort(arr[n] , p , q):                // [p , q] 表示对第 p ~ q 区域内的元素进行归并排序
# //     if p < q :                             // 对 [p , q] 区域不断采用对半分割的方式，最终将整个区域划分为多个仅包含 1 个元素（p==q）的序列
# //         mid = ⌊(p+q)/2⌋
# //         merge_sort(arr , p , mid)
# //         merge_sort(arr , mid+1 , q)
# //         merge(arr , p , mid , q)          // 调用实现归并过程的代码模块
# // merge_sort() 用于将整个序列分割成多个子序列，merge() 用来合并这些子序列，合并的实现方式为：
# // 从 [p, mid] 和 [mid+1, q] 两个区域的元素分别拷贝到 leftarr 和 rightarr 区域。
# // 从 leftarr 和 rightarr 区域中各个取出第一个元素，比较它们的大小；
# // 将较小的元素拷贝到 [p, q] 区域，然后从较小元素所在的区域内取出下一个元素，继续进行比较；
# // 重复执行第 3 步，直至 leftarr 和 rightarr 内的元素全部拷贝到 [p, q] 为止。如果 leftarr 或者 rightarr 有一方为空，则直接将另一方的所有元素依次拷贝到 [p, q] 区域。

# // 对应的伪代码如下：
# // merge(arr[n] , p , mid , q):                          // 该算法表示将 [p , mid] 和 [mid+1 , q] 做归并操作
# //     leftnum <- mid - p + 1                            // 统计 [p , mid] 区域内的元素个数
# //     rightnum <- q - mid                               // 统计 [mid+1 , q] 区域内的元素个数
# //     leftarr[leftnum] <- arr[p ... mid]                // 分别将两个区域内的元素各自拷贝到另外两个数组中
# //     rightarr[rightnum] <- arr[mid+1 ... q]
# //     i <- 1 , j <- 1
# //     for k <- p to q :             // 从 leftarr 和 rightarr 数组中第 1 个元素开始，比较它们的大小，将较小的元素拷贝到 arr 数组的 [p , q] 区域
# //         if leftarr[i] ≤ rightarr[j] :
# //             arr[k] = leftarr[i]
# //             i <- i+1
# //         else :
# //             arr[k] = right[j]
# //             j <- j+1

# //代码实现算法
#实现归并排序算法中的分割操作，[p,q]为指定分割区域
def merge_sort(arr,p,q):
    #列表中没有数据，或者 [p,q]区域不存在
    if len(arr) == 1 or p >= q:
        return
    #对 [p,q] 区域进行分割
    mid = int( (p + q) / 2 )
    merge_sort(arr,p,mid)
    merge_sort(arr,mid+1,q)
    #归并 [p,mid] 和 [mid+1,q] 区域
    merge(arr,p,mid,q)
#实现归并排序算法中的归并操作，归并区域为 [p.mid] 和 [mid+1,q]
def merge(arr,p,mid,q):
    numL = mid - p + 1;
    numR = q - mid;
    #分别将 [p,mid] 和 [mid+1,q] 区域内的元素拷贝到 leftarr 和 rightarr 列表中
    leftarr = arr[p-1:p+numL-1]
    rightarr = arr[mid:mid+numR]
    # 2 个列表末尾添加一个足够大的数
    leftarr.append(float('inf'))
    rightarr.append(float('inf'))
    i=0
    j=0
    k=p
    #逐个比较 leftarr 和 rightarr 列表中的元素，每次将较小的元素添加到 arr 列表中的 [p,q] 区域内
    while k <= q:
        if leftarr[i] <= rightarr[j]:
            arr[k-1] = leftarr[i]
            i = i + 1
        else:
            arr[k-1] = rightarr[j]
            j = j + 1
        k = k + 1

arr = [7, 5, 2, 4, 1, 6, 3, 0]
#对 arr 数组中第 1 至 8 个元素做归并排序操作
merge_sort(arr, 1, 8)
print(arr)
