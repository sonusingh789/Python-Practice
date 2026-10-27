class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
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

for i in range(10):
    ll.append(i)

ll.display()
