import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


def insert_at_tail(ll, node):
    """
    docstring
    """
    curr = ll.head
    if curr is None:
        ll.head = node
    else:
        while curr.next is not None:
            curr = curr.next
        curr.next = node


if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(125))
    
    ll = LinkedList()
    for item in items:
        insert_at_tail(ll, Node(item))

    print(items)
    print()
    print_nodes(ll)