from linked_list import LinkedListNode, LinkedList, makeN


dupes = LinkedList(LinkedListNode(0))
dupes.add(LinkedListNode(5))
dupes.add(LinkedListNode(10))
for n in range(0, 10):
    dupes.add(LinkedListNode(n))
    dupes.add(LinkedListNode(n+1))
    dupes.add(LinkedListNode(n+3))

# dupes.print_all()


def removeDupes(list):
    map = {}
    cur = dupes.first
    retList = LinkedList(LinkedListNode(cur.value))
    map[cur.value] = True

    while cur is not dupes.last:
        cur = cur.next
        if map.get(cur.value, None) is None:
            map[cur.value] = True
            retList.add(LinkedListNode(cur.value))
    return retList


# x = removeDupes(dupes)
# x.print_all()

def n_last(list, n):
    cur = list.first
    total = 1;
    while cur is not list.last:
        cur = cur.next
        total = total + 1
    # print('total:', total)

    if total < n+1:
        raise 'Index out of bounds'

    ret = list.first
    for x in range(total - n - 1):
        ret = ret.next
    return ret.value

nl = makeN(10)
# nl.print_all()
# print(n_last(nl, 0))
# print(n_last(nl, 1))
# print(n_last(nl, 9))




def sumList(l1, l2):
    sum = 0
    x = 1
    v1 = l1.first
    v2 = l2.first
    end = LinkedListNode(0)

    while v1 is not end and v2 is not end:
        sum += x * (v1.value + v2.value)
        x = x * 10
        if v1.next is not None:
            v1 = v1.next
        else:
            v1 = end;
        if v2.next is not None:
            v2 = v2.next
        else:
            v2 = end
    return num_to_back_list(sum)

def num_to_back_list(num):
    vals = []
    remaining = num
    while remaining > 0:
        next = remaining / 10
        vals.push(remaining - next * 10)
        next = remaining
    return vals


l1 = LinkedList(LinkedListNode(7))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(6))
l2 = LinkedList(LinkedListNode(5))
l2.add(LinkedListNode(9))
l2.add(LinkedListNode(2))
print(sumList(l1, l2))
