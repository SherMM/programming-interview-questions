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