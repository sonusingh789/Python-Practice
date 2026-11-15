class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    # insertion at the beg

    def appendbeg(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def deletebeg(self):
        if self.head == None:
            print("list is Empty")
            return
        self.head = self.head.next

    def deletepos(self, pos):
        if self.head == None:
            print("list is Empty")
            return
        if pos == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0
        while curr.next != None and count < pos - 1:
            count += 1
            curr = curr.next
        if curr.next == None:
            print("Invalid Position")
            return
        curr.next = curr.next.next

    def delete_end(self):
        if self.head == None:
            print("List is Empty")
            return
        if self.head.next == None:
            self.head = None
            return

        curr = self.head

        while curr.next.next != None:
            curr = curr.next
        curr.next = None
