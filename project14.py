# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:50:35 2026
Q4. Build a Stack class. Write a class Stack with methods push(x), pop(), peek(), is_empty() and size(). pop() and peek() on an empty stack should raise IndexError with a clear message.
Q5. Build a Queue class. Write a class Queue (using deque) with enqueue(x), dequeue(), front(), is_empty() and size(). Dequeuing from an empty queue should raise IndexError.
Q6. Balanced brackets. Write is_balanced(s) that returns True if every (, [, { in s is closed in the right order. Test with "{[()]}" (True), "([)]" (False), "((" (False), "" (True).
Q7. Reverse with a stack. Write reverse_string(s) using only stack operations (no slicing, no reversed()). Then use it to write is_palindrome(s).
Q8. Hot potato (queue simulation). Players ["A", "B", "C", "D", "E"] stand in a circle. The potato is passed k times, and whoever holds it is out. Repeat until one player is left. Write hot_potato(players, k) that returns the winner using a queue. What is the winner for k = 3?
Q9. Queue using two stacks. Implement a QueueTwoStacks class with enqueue and dequeue using only two Python lists used as stacks (only append and pop()). Explain why each item is moved at most twice.
Q10. Min stack. Design a MinStack that supports push, pop, top and get_min, where every operation runs in O(1) time. Push 5, 3, 7, 3, 1, then pop twice: what does get_min() return after each step
@author: Admin
"""

from collections import deque

# Q4
class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

def test_stack():
    s = Stack()
    assert s.is_empty() == True
    s.push(10)
    s.push(20)
    assert s.size() == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty() == True
    print(" Stack tests passed!")

# Q5
class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, x):
        self._items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)

def test_queue():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue("a")
    q.enqueue("b")
    assert q.size() == 2
    assert q.front() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.is_empty() == True
    print(" Queue tests passed!")

# Q6
def is_balanced(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
            
    return len(stack) == 0


def test_balanced_brackets():
    assert is_balanced("{[()]}") == True
    assert is_balanced("([)]") == False
    assert is_balanced("((") == False
    assert is_balanced("") == True
    print(" Balanced Brackets tests passed!")

# Q7
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())
    return "".join(reversed_chars)

def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == reverse_string(cleaned)

# Verification & Tests for Q7
def test_reverse_and_palindrome():
    assert reverse_string("hello") == "olleh"
    assert is_palindrome("Racecar") == True
    assert is_palindrome("hello") == False
    print(" Reverse & Palindrome tests passed!")

# Q8
def hot_potato(players, k):
    q = deque(players)
    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())
        q.popleft()  
    return q[0]

def test_hot_potato():
    players = ["A", "B", "C", "D", "E"]
    winner = hot_potato(players, 3)
    assert winner == "A"
    print(f" Hot Potato test passed! Winner for k=3: {winner}")

# Q9
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()

def test_queue_two_stacks():
    q2 = QueueTwoStacks()
    q2.enqueue(1)
    q2.enqueue(2)
    assert q2.dequeue() == 1
    q2.enqueue(3)
    assert q2.dequeue() == 2
    assert q2.dequeue() == 3
    print(" QueueTwoStacks tests passed!")

# Q10
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]

def test_min_stack():
    min_stack = MinStack()
    for val in [5, 3, 7, 3, 1]:
        min_stack.push(val)
    
    min_stack.pop()  # Pop 1st time (removes 1)
    assert min_stack.get_min() == 3
    
    min_stack.pop()  # Pop 2nd time (removes 3)
    assert min_stack.get_min() == 3
    print(" MinStack tests passed!")

if __name__ == "__main__":
    test_stack()
    test_queue()
    test_balanced_brackets()
    test_reverse_and_palindrome()
    test_hot_potato()
    test_queue_two_stacks()
    test_min_stack()
    print("\nAll verifications and test suites completed successfully!")
