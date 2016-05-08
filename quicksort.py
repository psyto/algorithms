#quicksort

def quicksort(array):
    if len(array) < 1:
        return array
    pivot = array[0]
    left = []
    right = []
    for x in range(1, len(array)):
        if array[x] <= pivot:
            left.append(array[x])
        else:
            right.append(array[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

