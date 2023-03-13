# Sorting algorithm: selection sort

def selection_sort(L):
    """(list) -> NoneType
        Sort the items of L from smallest to largest.
    >>> L = [9, 3, 7, 2, 5, 1]
    >>> selection_sort(L)
    [1, 2, 3, 5, 7, 9]
    >>> L = [1.5, 0, 11, 12, 5, 1]
    >>> selection_sort(L)
    [0, 1, 1.5, 5, 11, 12]
    """

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                idx_of_smallest = j     # use a mediator to help switch values
                L[i], L[idx_of_smallest] = L[idx_of_smallest], L[i]
    return L


