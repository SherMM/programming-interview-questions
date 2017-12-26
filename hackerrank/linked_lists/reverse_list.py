import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


def reverse(ll):
    """
    docstring
    """
    prev = None
    curr = ll.head
    while curr is not None:
        temp = curr.next 
        curr.next = prev
        prev = curr
        curr = temp
    ll.head = prev


if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(151))

    ll = LinkedList()
    for item in items:
        ll.push(Node(item))

    print_nodes(ll)
    print()
    reverse(ll)
    print_nodes(ll)
