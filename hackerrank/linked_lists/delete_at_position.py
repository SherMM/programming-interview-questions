import sys
import random
from linked_list import LinkedList, Node
from print_nodes import print_nodes


if __name__ == "__main__":
    n = int(sys.argv[1])
    items = []
    for _ in range(n):
        items.append(random.randrange(150))
    
    print(items)
    ll = LinkedList()
    for item in items:
        ll.push(Node(item))
    
    print("original list")
    print_nodes(ll)
    pos = random.randrange(n)
    print("deleting at index: {}".format(pos))
    ll.delete(pos)
    print_nodes(ll)