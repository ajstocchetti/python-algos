def quicksort(list):
    return quick_sort_recursive(list, 0, len(list) - 1)

quick_sort_recursive(list, first, last):
    if last - first < 2:
        # 0 or 1 elements
        return list
    # for now, pick first element as pivot
    pivot = first
    smaller = pivot
    larger = pivot
    for n in range(pivot+1, last+1):
        if list[n] > list[pivot]:
            larger += 1
        else:


    #
    quick_sort_recursive(list, ??, ??)
    quick_sort_recursive(list, ??, ??)
    return list
