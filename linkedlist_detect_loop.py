# How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle?
# Sample linked-list: 1 -> 2 -> 3 -> 4 -> 5 -> 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def detect_loop(self):
        past = set()
        node = self.head
        while node:
            if node.data in past:
                return node
            else:
                past.add(node.data)
                node = node.next

# Preparation: create the SinglyLinkedList according to a given data
s = [1, 2, 3, 4, 5, 3]
sll = SinglyLinkedList()
for x in reversed(s): sll.push(x)

# detect loop
if sll.head is not None:
    node = sll.detect_loop()
    if node is not None:
        print('Found a loop starting at node: ', node.data)
    else:
        print('There is no loop in the linked list.')