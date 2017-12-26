import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


def get_kth_node_value(ll, k):
    """
    advance pointer k positions ahead
    """
    c = 0
    p1 = ll.head
    while c <= k and p1 is not None:
        c += 1
        p1 = p1.next
    
    p2 = ll.head
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    if p2 is None:
        return p2
    return p2.data



if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(150))


    ll = LinkedList()
    for item in items:
        ll.push(Node(item))

    ll = LinkedList()
    k = random.randrange(n)
    print_nodes(ll)
    print()
    print("k: {}".format(k))
    print(get_kth_node_value(ll, k))