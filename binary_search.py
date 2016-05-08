#binary_search

def binary_search(input_array, value):
    """Your code goes here."""
    lowerbound = 0
    upperbound = len(input_array) - 1
    while lowerbound <= upperbound:
        m = (lowerbound + upperbound) / 2
        if input_array[m] < value:
            lowerbound = m + 1
        elif input_array[m] > value:
            upperbound = m - 1
        else:
            return m
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
