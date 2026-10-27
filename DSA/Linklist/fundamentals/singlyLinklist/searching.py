class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    # insert at beg
    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    def search(self, data):
        curr = self.head

        while curr != None:
            if curr.data == data:
                return 1
            curr = curr.next
        return -1


ll = LinkList()

for i in range(40):
    ll.append(i)

print(ll.search(5))
