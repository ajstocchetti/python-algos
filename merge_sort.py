def merge_sort(list):
    # print('calling merge_sort')
    if len(list) is 1:
        return list
    mid = len(list) // 2
    # print('here', list, mid)
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:])
    ret = []
    i = 0
    j = 0
    while (i < len(left)) or (j < len(right)):
        if i is len(left):
            ret.append(right[j])
            j = j + 1
        elif j is len(right):
            ret.append(left[i])
            i = i + 1
        elif left[i] < right[j]:
            ret.append(left[i])
            i = i + 1
        else:
            ret.append(right[j])
            j = j + 1
    return ret



x = merge_sort([2,5,7,8,4,1,9,3,6])
print('Final answer:', x)
