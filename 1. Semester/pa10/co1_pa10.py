def quicksort(lst, pivotFunction, lo=0, hi=-1):
    if hi == -1:
        hi = len(lst)-1

    if lo < hi:
        p = partition(lst, lo, hi, pivotFunction)
        quicksort(lst, pivotFunction, lo, p)
        quicksort(lst, pivotFunction, p + 1, hi)
    else:
        return

def partition(lst, lo, hi, pivotFunction):
    pivot = pivotFunction(lst, lo, hi)

    i = lo
    for j in range(lo, hi+1):
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
        if lst[j] == pivot:
            lst[j], lst[i] = lst[i], lst[j]
    return i