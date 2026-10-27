class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append_beg(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append_pos(self, data, k):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        curr = self.head
        count = 0
        while curr.next != None and count < k - 1:
            count += 1
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def append_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node

    def display(self):

        curr = self.head
        while curr != None:
            print(curr.data, end=" --> ")
            curr = curr.next
        print("None")


ll = LinkList()

ll.append_beg(5)
ll.append_beg(4)
ll.append_end(7)
ll.append_pos(8, 2)
ll.display()
# 4 --> 5 --> 8 --> 7 --> None
