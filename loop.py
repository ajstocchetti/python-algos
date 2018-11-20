from linked_list import LinkedList,LinkedListNode,makeN

def get_loop_node(list):
    # step 1: get in the loop
    fast = list.first
    slow = list.first

    while True:
        if fast.next is None:
            print('returining none')
            return None
        fast = fast.next
        if fast.next is None:
            print('returining none')
            return None
        fast = fast.next
        slow = slow.next
        if fast is slow:
            break

    #step 2: go through loop making a hash
    map = {}
    first = slow
    while True:
        if map.get(id(slow), None):
            break
        map[id(slow)] = True
        slow = slow.next

    # step 3: start at beginning and go to loop
    finder = list.first
    while True:
        if map.get(id(finder), None):
            print('returining finder')
            return finder
        finder = finder.next


print('None:', get_loop_node(makeN(17)))

looped = LinkedList(LinkedListNode(5))
for i in range(10):
    looped.add(LinkedListNode(i))
node = LinkedListNode(17)
looped.add(node)
for i in range(20, 25):
    looped.add(LinkedListNode(i))
looped.add(node)
print('17:', get_loop_node(looped).value)
