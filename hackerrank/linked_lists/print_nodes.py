import sys
import random
from linked_list import LinkedList, Node


def print_nodes(ll):
    """
    docstring
    """
    curr = ll.head
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print()
        

if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(25))
    
    ll = LinkedList()
    for item in items:
        ll.push(Node(item))

    print("items to add:")
    print(items)
    print()
    print("linked list:")
    print_nodes()
