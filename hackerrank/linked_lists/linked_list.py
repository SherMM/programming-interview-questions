class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1

    def insert(self, node, i):
        c = 0
        prev = None
        curr = self.head
        while c < i and i < self.length:
            c += 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = node
        else:
            self.head = node
        node.next = curr
        self.length += 1

    def delete(self, i):
        c = 0
        prev = None
        curr = self.head
        while c < i and i < self.length:
            c += 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
        self.length -= 1