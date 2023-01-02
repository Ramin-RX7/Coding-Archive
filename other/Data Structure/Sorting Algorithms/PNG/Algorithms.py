def bubble_sort(array):
    """
    O(n^2) :   n(n-1) / 2
    Bubble sort consists of making multiple passes through a list,
      comparing elements one by one, and swapping adjacent items that are out of order.
    At the end of iteration 1, the max element will be placed at the last index of the array.
      We continue the same process n-1 times for the remaining unsorted array.    
    """
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        #   terminate early if there's nothing left to sort
        # (This is not nesseccary, just to increase algorithm speed)
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            # If the item you're looking at is greater than its adjacent value:
            if array[j] > array[j + 1]:
                # then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


def insetion_sort(array):
    """
    O(n^2) But better than Bubble Sort
    It builds the sorted list one element at a time by comparing each item with 
      the rest of the list and inserting it into its correct position.
    """
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1
        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1
        #Instead of code below We can do this in python with lists:
        # array.insert(j+1,key_item)

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array



def merge(left, right):
    """
    O(n.lg(n))  lg(n) cause we devide it by 2 halves -- n for doing it for each item (at most is n)
    Conceptually, a merge sort works as follows:
      1) Divide the unsorted list into n sublists, each containing one element 
           (a list of one element is considered sorted).
      2) Repeatedly merge sublists to produce new sorted sublists
           until there is only one sublist remaining. This will be the sorted list.
    """
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result
def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))



def quicksort(array):
    """
    O(n.lg(n))
    divide (partitioning) the input array into two lists, the first with small items and 
      the second with large items.
    The algorithm then sorts both lists recursively until 
      the resultant list is completely sorted.
    """
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Selecting `pivot`
    pivot = array[0]
    # from random import randint
    # pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)



