def inversion_ms(list):
    if len(list) <= 1:
        return {'a': list, 'c': 0}

    mid = len(list)//2
    l = inversion_ms(list[0:mid])
    r = inversion_ms(list[mid:])

    x = 0
    i = 0
    j = 0
    invs = l['c'] + r['c']
    merged = []
    while x < len(list):
        x = x+1
        if i is len(l['a']):
            merged.append(r['a'][j])
            j = j+1
            continue
        elif j is len(r['a']):
            merged.append(l['a'][i])
            i = i+1
            continue
        elif l['a'][i] < r['a'][j]:
            merged.append(l['a'][i])
            i = i+1
            continue
        else:
            merged.append(r['a'][j])
            j = j+1
            invs += len(l['a']) - i
    return {'a':merged, 'c': invs}




def count_inversions(list):
    ans = inversion_ms(list)
    print(list, ans['c'])
    return ans['c']

count_inversions([2,5,7,8,4,1,9,3,6])
count_inversions([1,3,5,2,4,6])
