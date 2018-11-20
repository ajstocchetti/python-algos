class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None
    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, init):
        self.first = init
        self.last = init

    def add(self, next):
        self.last.set_next(next)
        self.last = next

    def remove(self, index):
        if index < 0:
            raise 'Index out of bounds - low'
        if index is 0:
            self.first = self.first.next
            return
        cur = self.first
        x = 0
        while x < index - 1:
            if cur.next is None:
                raise 'Index out of bounds - high'
            cur = cur.next
            x = x + 1
        remove = cur.next
        cur.next = remove.next
    def print_all(self):
        cur = self.first
        while(True):
            print(cur.value)
            if cur.next is None:
                break
            cur = cur.next
        print("\n")



def makeN(n):
    list = LinkedList(LinkedListNode(0))
    for n in range(1, n):
        list.add(LinkedListNode(n))
    return list
