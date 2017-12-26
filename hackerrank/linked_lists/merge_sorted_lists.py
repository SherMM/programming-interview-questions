import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


def merge(l1, l2):
    """
    docstring
    """
    p1 = l1.head
    p2 = l2.head
    ll = LinkedList()
    while p1 and p2:
        if p1.data < p2.data:
            ll.push(Node(p1.data))
            p1 = p1.next
        else:
            ll.push(Node(p2.data))
            p2 = p2.next

    while p1:
        ll.push(Node(p1.data))
        p1 = p1.next
    while p2:
        ll.push(Node(p2.data))
        p2 = p2.next
    return ll


if __name__ == "__main__":
    n, m = int(sys.argv[1]), int(sys.argv[2])
    items1 = []
    for _ in range(n):
        items1.append(random.randrange(151))

    items2 = []
    for _ in range(m):
        items2.append(random.randrange(151))

    items1.sort(reverse=True)
    items2.sort(reverse=True)

    l1 = LinkedList()
    for item in items1:
        l1.push(Node(item))

    l2 = LinkedList()
    for item in items2:
        l2.push(Node(item))

    print_nodes(l1)
    print_nodes(l2)
    ll = merge(l1, l2)
    print()
    print_nodes(ll)