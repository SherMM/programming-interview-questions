import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


def insert_at_head(ll, node):
    """
    docstring
    """
    curr = ll.head 
    if curr is None:
        ll.head = node
    else:
        node.next = curr
        ll.head = node
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(150))

    ll = LinkedList()
    for item in items:
        insert_at_head(ll, Node(item))

    print(items)
    print()
    print_nodes(ll)