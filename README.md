# linkedlist-detect-loop
How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle?
Sample linked-list: 1 -> 2 -> 3 -> 4 -> 5 -> 3  ==>  found cycle starting at node 3.

Tips: keep tracking all nodes while traverse the linked list, until a traversed node appears again, so a loop is found. Otherwise, no loop in the linked list. 
