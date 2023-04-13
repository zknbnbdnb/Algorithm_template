# @Time    : 2021/12/20 16:05
# @Author  : 康带帅
# @FileName: 10大排序.py
# @Software: PyCharm
# @Blog    ：https://github.com/zknbnbdnb
import random
import time

# ***********************比较排序******************************** #


def InsertSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    length = len(mylist)
    for i in range(1, length):
        # 设定当前元素的一个标识值
        j = i -1
        # 如果当前值小于一个元素，将当前值临时存储，将前一个元素后移一位
        if mylist[i] < mylist[j]:
            temp = mylist[i]
            mylist[i] = mylist[j]
            # 往前继续寻找，找到比临时变量小的下标，整体后移
            j -= 1
            while j >= 0 and mylist[j] > temp:
                mylist[j + 1] = mylist[j]
                j -= 1
            mylist[j + 1] = temp
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def BinInsertSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    for i in range(1, len(mylist)):
        low, high = 0, i - 1
        temp = mylist[i]
        while low <= high:
            mid = low + (high - low) // 2
            if mylist[mid] < temp:
                low = mid + 1
            else:
                high = mid - 1
        j = i - 1
        while j > high:
            mylist[j + 1] = mylist[j]
            j -= 1
        mylist[high + 1] = temp
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def ShellSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    length= len(mylist)
    gap = length // 2
    while gap >= 1:
        for j in range(gap, length):
            i = j
            while(i - gap) >= 0:
                if mylist[i] < mylist[i - gap]:
                    mylist[i], mylist[i - gap] = mylist[i - gap], mylist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

# ***********************交换排序******************************** #

def BubbleSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    length = len(mylist)
    while length > 0:
        length -= 1
        cur = 0
        while cur < length:
            if mylist[cur] > mylist[cur + 1]:
                mylist[cur], mylist[cur + 1] = mylist[cur + 1], mylist[cur]
            cur += 1
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def QuickSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    low, high = 0, len(mylist) - 1
    def quickSort(mylist, low, high):
        if low >= high:
            return mylist
        pivot = mylist[low]
        i, j = low, high
        while low < high:
            while low < high and mylist[high] >= pivot:
                high -= 1
            mylist[low] = mylist[high]
            while low < high and mylist[low] <= pivot:
                low += 1
            mylist[high] = mylist[low]
        mylist[high] = pivot
        quickSort(mylist, i, low - 1)
        quickSort(mylist, low + 1, j)
    # ******************************************************* #
    quickSort(mylist, low, high)
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

# ***********************选择排序******************************** #

def SelectSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    count = len(mylist)
    for i in range(count):
        for j in range(i + 1, count):
            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def mergeSort(mylist):
    # ******************************************************* #
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    def marge_sort(mylist):
        if len(mylist) <= 1:
            return mylist
        mid = len(mylist) // 2
        left = marge_sort(mylist[:mid])
        right = marge_sort(mylist[mid:])
        return merge(left, right)
    # ******************************************************* #
    start = time.perf_counter()
    mylist = marge_sort(mylist)
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def heapSort(mylist):
    # ******************************************************* #
    def adjustHeap(mylist, i, length):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        max = i
        if i < length // 2:
            if left_child < length and mylist[left_child] > mylist[max]:
                max = left_child
            if right_child < length and mylist[right_child] > mylist[max]:
                max = right_child
            if max != i:
                mylist[max], mylist[i] = mylist[i], mylist[max]
                adjustHeap(mylist, max, length)
    def buildHeap(mylist, length):
        for i in range(0, length // 2)[::-1]:
            adjustHeap(mylist, i, length)
    def heapsort(mylist):
        length = len(mylist)
        buildHeap(mylist, length)
        for i in range(length)[::-1]:
            mylist[0], mylist[i] = mylist[i], mylist[0]
            adjustHeap(mylist, 0, i)
        return mylist
    # ******************************************************* #
    start = time.perf_counter()
    mylist = heapsort(mylist)
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def radixSort(mylist):
    start = time.perf_counter()
    # ******************************************************* #
    maxlength = len(str(max(mylist)))
    for i in range(maxlength):
        radix = [[] for _ in range(10)]
        for j in mylist:
            radix[j // (10 ** i) % 10].append(j)
        mylist = [k for j in radix for k in j]
    # ******************************************************* #
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

def bucketSortORcountSort(mylist):
    def helpQS(mylist, low, high):
        if low >= high:
            return mylist
        pivot = mylist[low]
        i, j = low, high
        while low < high:
            while low < high and mylist[high] >= pivot:
                high -= 1
            mylist[low] = mylist[high]
            while low < high and mylist[low] <= pivot:
                low += 1
            mylist[high] = mylist[low]
        mylist[high] = pivot
        help(mylist, i, low - 1)
        help(mylist, low + 1, j)
    start = time.perf_counter()
    flag = 0
    n = 10 if flag else 1
    low, high = min(mylist), max(mylist)
    bucket_num = (high - low + 1) // n
    bucket = [[] for _ in range(bucket_num)]
    for i in mylist:
        bucket[(i - low) // n].append(i)
    mylist = []
    for j in bucket:
        helpQS(j, 0, len(j) - 1)
        # j.sort()
    for j in bucket:
        if len(j):
            mylist.extend(j)
    end = time.perf_counter()
    if len(mylist) <= 30:
        print(mylist)
    print(end - start)
    print()

if __name__ == '__main__':
    n = 5000
    a = list(range(n))
    random.shuffle(a)
    mylist = a
    # print(mylist)
    print()
    InsertSort(mylist.copy())
    BinInsertSort(mylist.copy())
    ShellSort(mylist.copy())
    BubbleSort(mylist.copy())
    QuickSort(mylist.copy())
    SelectSort(mylist.copy())
    mergeSort(mylist.copy())
    heapSort(mylist.copy())
    radixSort(mylist.copy())
    bucketSortORcountSort(mylist.copy())


























