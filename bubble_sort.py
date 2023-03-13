# Sorting algorithm: bubble sorting

def bubble_sort(L):
    """(list of integers)->(list of integers)
    return a sorted list of integers in ascending order.
    >>> L = [4, 3, 5, 1, 7]
    >>> bubble_sort(L)
    [1, 3, 4, 5, 7]
    >>> L = [6, 1, 2, 7, 4, 3, 5]
    >>> bubble_sort(L)
    [1, 2, 3, 4, 5, 6, 7]
    """
    stopper = len(L) - 1
    while stopper > 0:
        for i in range(0, stopper):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        stopper -= 1

    return L

if __name__ == '__main__':
    import doctest
    doctest.testmod()
