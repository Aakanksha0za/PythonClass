# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:53:42 2026
class Node:
def __init__(self, data):
self.data = data
self.next = None
Q6. Build and print a linked list(Easy)
Write a LinkedList class with append(data) , which adds a node at the end, and
display() , which prints the list as 10 -> 20 -> 30 -> None .
ll = LinkedList()
ll.append(10); ll.append(20); ll.append(30)
ll.display() # 10 -> 20 -> 30 -> None
Q7. Insert at beginning, count nodes, search (Easy)
Add three methods to your LinkedList class:
insert_at_beginning(data)
length() , which returns the number of nodes. Don't use a counter variable stored in
the class.
search(key) , which returns True if key is in the list and False otherwise.
ll.insert_at_beginning(5)
ll.display() # 5 -> 10 -> 20 -> 30 -> None
print(ll.length()) # 4
print(ll.search(20)) # True
print(ll.search(99)) # False
Q8. Delete a node by value (Medium)
Write delete(key) , which removes the first node containing key . Your method must
handle these cases:
Python Practice: Stacks, Queues & Linked Lists
the list is empty
the node to delete is the head
the key isn't in the list (print "Not found" )
ll.delete(5) # deleting head
ll.delete(20) # deleting middle
ll.delete(99) # Not found
ll.display() # 10 -> 30 -> None
Q9. Reverse a linked list(Medium)
Write reverse() , which reverses the list in place by changing the next pointers. Don't
create new nodes and don't copy the data into a Python list.
# list: 1 -> 2 -> 3 -> 4 -> None
ll.reverse()
ll.display() # 4 -> 3 -> 2 -> 1 -> None
Q10. Find the middle node and detect a cycle (Hard)
(a) Write find_middle() , which returns the middle node's data in a single pass. Use two
pointers, one slow and one fast. For an even number of nodes, return the second middle.
(b) Write has_cycle() , which returns True if the list contains a loop. Use Floyd's
slow/fast pointer method.
# 1 -> 2 -> 3 -> 4 -> 5 -> None
print(ll.find_middle()) # 3
# 1 -> 2 -> 3 -> 4 -> None
print(ll.find_middle()) # 3
ll.head.next.next.next.next = ll.head.next # create a loop: 4 -> 2
print(ll.has_cycle()) # True
Warning: don't call display() on a list with a cycle. It will loop forever
@author: Admin
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Q6: Append a node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Q6: Display list as 10 -> 20 -> 30 -> None
    def display(self):
        current = self.head
        parts = []
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        parts.append("None")
        print(" -> ".join(parts))

    # Q7: Insert a new node at the beginning (head)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Q7: Count nodes by traversing (no stored counter attribute)
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # Q7: Search for key and return True/False
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    # Q8: Delete first node containing key
    def delete(self, key):
        if self.head is None:
            print("Not found")
            return

        # Case 1: The head itself holds the key
        if self.head.data == key:
            self.head = self.head.next
            return

        # Case 2: Search for key in remaining nodes
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        # Case 3: Key not found
        print("Not found")

    # Q9: Reverse the linked list in place by rewiring next pointers
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse pointer
            prev = current            # Advance prev
            current = next_node       # Advance current
        self.head = prev

    # Q10(a): Return middle node's data in a single pass (second middle if even)
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    # Q10(b): Detect cycle using Floyd's tortoise-and-hare algorithm
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    ll = LinkedList()

    # Q6: append & display
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    print("After append:")
    ll.display()

    # Q7: insert_at_beginning, length & search
    ll.insert_at_beginning(5)
    print("After insert_at_beginning(5):")
    ll.display()
    print("Length:", ll.length())
    print("Search 20:", ll.search(20))
    print("Search 99:", ll.search(99))

    # Q8: delete
    ll.delete(5)   # Head node
    ll.delete(20)  # Middle node
    ll.delete(40)  # Tail node
    ll.delete(99)  # Missing node -> prints "Not found"
    print("After deletes:")
    ll.display()

    # Q9: reverse
    ll.reverse()
    print("After reverse:")
    ll.display()

    # Q10(a): find_middle
    print("Middle (even length):", ll.find_middle())
    ll.append(50)
    print("Middle (odd length):", ll.find_middle())

    # Q10(b): has_cycle
    print("Has cycle (no cycle):", ll.has_cycle())

    # Create a cycle (tail -> second node) to test True case
    tail = ll.head
    while tail.next is not None:
        tail = tail.next
    tail.next = ll.head.next
    print("Has cycle (with cycle):", ll.has_cycle())