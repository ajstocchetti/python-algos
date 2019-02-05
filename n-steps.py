def n_steps(n):
    if n <= 0:
        return 1
    list = [1, 2, 4]
    while len(list) < n:
        list.append(sum_last_3(list))
    return list[n - 1]

def sum_last_3(arr):
    l = len(arr)
    return arr[l-1] + arr[l-2] + arr[l-3]



for x in range(0, 10):
    print (n_steps(x))
