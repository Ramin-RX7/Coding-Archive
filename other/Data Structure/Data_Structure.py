import rx7 as rx
from pprint import pprint

def make_random_list(n,first=0,last=0):
    if not last:  last=n
    a = []
    for i in range(n):
        a.append(rx.random.integer(first,last))
    return a


# t = rx.record()

# print(t.lap())


# exit()














def bubble_sort(array):  # O(n^2)
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insertion_sort(array):  # O(n^2)
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
          array[j + 1] = array[j]
          j -= 1
        array[j + 1] = key_item
        # array.insert(j+1,key_item)
    return array


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result
def merge_sort(array):  # O(n.lg(n))
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def quicksort(array):
    if len(array) <= 1:
        return array
    low, same, high = [], [], []
    pivot = array[0]
    for item in array:
        if item < pivot:     low.append(item)
        elif item == pivot:  same.append(item)
        elif item > pivot:   high.append(item)
    return quicksort(low) + same + quicksort(high)


def LinearSearch(lst, element):
    for i in range (len(lst)):
        if lst[i] == element:
            return i
    return -1


def BinarySearch(lst, val):
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == val:
            index = mid
        else:
            if val<lst[mid]:
                last = mid -1
            else:
                first = mid +1
    return index





"""
Bubble:      1_000   ... 15_000       :  1000
Insertion:   1_000   ... 20_000       :  1000
Merge:       100_000 ... 2_500_000   :  150_000
Quick:       250_000 ... 4_000_000   :  250_000
"""

def Range(a,b): return range(a,b+1)
Groups = {
    "Bubble"    :   list(Range(1_000,15_000))[::1000],
    "Insertion" :   list(Range(1_000,20_000))[::1000],
    "Merge"     :   list(Range(50_000,1_000_000))[::50_000],
    "Quick"     :   list(Range(150_000,2_400_000))[::150_000],
    
    "Linear"    :   list(Range(500_000,7_000_000))[::500_000],
    "Binary"    :   list(Range(10_000_000,100_000_000))[::5_000_000]
}






t = rx.record()
TIMES = []
lst = list(range(100_000_000))
print(t.lap())
BinarySearch(lst,-1)
print(t.last_lap())
exit()
for n in Groups["Binary"]:
    lst = list(range(n))
    t = rx.record()
    BinarySearch(lst,-1)
    # TIMES.append(t.last_lap())
    print(t.lap())
# BinarySearch(make_random_list(500_000),-1)    

pprint(TIMES)
print(t.lap())














