# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:29:54 2026

@author: Admin
"""

class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Initially points to nothing

# 2. Define the Linked List manager
class LinkedList:
    def __init__(self):
        self.head = None  # The start of the list is initially empty

    # Insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Link the last node to the new node
        current.next = new_node

    # Print the full linked list
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# --- Using the Linked List ---
ll = LinkedList()
ll.append("Node A")
ll.append("Node B")
ll.append("Node C")

ll.display()  # Output: Node A -> Node B -> Node C -> None