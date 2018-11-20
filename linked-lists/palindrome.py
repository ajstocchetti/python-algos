from linked_list import LinkedList,LinkedListNode


def is_palindrome(list):
    # if is a palandrome, is same forewards as backwards
    arr = []
    cur = list.first
    while cur is not None:
        arr.append(cur.value)
        cur = cur.next
    cur = list.first
    index = len(arr) - 1
    while cur is not None:
        if arr[index] is not cur.value:
            return False
        index = index - 1
        cur = cur.next
    return True


pList = LinkedList(LinkedListNode(1))
pList.add(LinkedListNode(2))
pList.add(LinkedListNode(3))
pList.add(LinkedListNode(4))
pList.add(LinkedListNode(3))
pList.add(LinkedListNode(2))
pList.add(LinkedListNode(1))

notP = LinkedList(LinkedListNode(1))
notP.add(LinkedListNode(2))
notP.add(LinkedListNode(3))
notP.add(LinkedListNode(4))

print('palantrome', is_palindrome(pList))
print('not pal', is_palindrome(notP))


def intersecting(list1, list2):
    last1 = list1.first
    while last1.next is not None:
        last1 = last1.next
    last2 = list2.first
    while last2.next is not None:
        last2 = last2.next
    if last1 is last2:
        return getIntersecting(list1, list2)
    else:
        return None
def getIntersecting(list1, list2):
    val1 = list1.first
    while val1 is not None:
        val2 = list2.first
        while val2 is not None:
            if val2 is val1:
                return val1
            val2 = val2.next
        val1 = val1.next
    raise 'Didnt find it, but should have'

def intersecting2(list1, list2):
    dict = {}
    cur = list1.first
    while cur is not None:
        dict[id(cur)] = True
        cur = cur.next
    cur = list2.first
    while cur is not None:
        if dict.get(id(cur), None) is not None:
            return cur
        cur = cur.next
    return None

node = LinkedListNode('a')
l1 = LinkedList(LinkedListNode(0))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))
l1.add(LinkedListNode(1))

l2 = LinkedList(LinkedListNode(0))
l2.add(LinkedListNode(1))
l2.add(LinkedListNode(1))
l2.add(LinkedListNode(1))
l2.add(LinkedListNode(1))
l2.add(node)
l2.add(LinkedListNode(1))
l2.add(LinkedListNode(1))
l2.add(LinkedListNode(1))

l3 = LinkedList(LinkedListNode(0))
l3.add(LinkedListNode(1))
l3.add(LinkedListNode(1))
l3.add(LinkedListNode(1))
l3.add(node)

print('should be none', intersecting(l1, l2))
print('should be none', intersecting(l1, l3))
print('should be node a:', intersecting(l2, l3).value)
print('should be none', intersecting2(l1, l2))
print('should be none', intersecting2(l1, l3))
print('should be node a:', intersecting2(l2, l3).value)
