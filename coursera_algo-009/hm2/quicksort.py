#head, tail, median
def partition(array, head, tail, pivot_choosing):
    if pivot_choosing == "tail":
        temp = array[head]
        array[head] = array[tail]
        array[tail] = temp
    elif pivot_choosing == "median":
        first = array[head]
        last = array[tail]
        mid_pos = head + ((tail - head) / 2)
        middle = array[mid_pos]
        pivot = -1
        if (first < last and first > middle) or (first < middle and first > last):
            pivot = head
        elif (middle < last and middle > first) or (middle < first and middle > last):
            pivot = mid_pos
        else:
            pivot = tail

        temp = array[head]
        array[head] = array[pivot]
        array[pivot] = temp

    pivot = head
    i = head + 1
    j = head + 1

    temp = array[head]
    array[head] = array[pivot]
    array[pivot] = temp

    pivot_value = array[head]
    while j <= tail:
        if array[j] < pivot_value:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i + 1
        j = j + 1

    temp = array[i - 1]
    array[i - 1] = array[head]
    array[head] = temp

    return array, i - 1

def QuickSort(array, head, tail, count, pivot_choosing):

    if tail - head < 1 :
        return array, count
    new_count = count + (tail - head)
    #head, tail, median
    new_array, pivot = partition(array, head, tail, pivot_choosing)

    new_array, new_count = QuickSort(new_array, head, pivot - 1, new_count, pivot_choosing)
    new_array, new_count = QuickSort(new_array, pivot + 1, tail, new_count, pivot_choosing)
    return new_array, new_count


with open("QuickSort.txt", "r") as f:
    test_array = [int(num) for num in f.readlines()]

length = len(test_array)

#array, count = QuickSort(test_array, 0, length - 1, 0, "head")
#print count

#array, count = QuickSort(test_array, 0, length - 1, 0, "tail")
#print count

array, count = QuickSort(test_array, 0, length - 1, 0, "median")
print count
