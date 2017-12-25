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
        if ll.length == 0:
            pos = 0
        else:
            pos = random.randrange(ll.length)
        print("inserting at index: {}".format(pos))
        ll.insert(Node(item), pos)
        print_nodes(ll)
    