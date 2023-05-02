# Using Python's deque module, implement a queue.

from collections import deque

class queue:
    def __init__(self):
        self.data = deque() # instantiate the class

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft() # pop from the opposite direction

# Test cases:
myQueue = queue()
myQueue.enqueue(3)
myQueue.enqueue(6)
myQueue.enqueue(9)
print(myQueue.dequeue()) # 3
print(myQueue.dequeue()) # 6
print(myQueue.dequeue()) # 9



# Hint: push/pop operations in a queue happen on the opposite sides. Picture standing in a line -- you start at the back of the line, and leave the line once you reach the front! Using deque, you can choose your own mapping of left/right to the front/back of the line. Either way (left -> front, right -> back or vice versa) works!

# Useful built-in deque methods:
# append: add an element to the right side
# appendleft: add an element from the left side
# pop: add an element to the right side
# popleft: add an element from the left side