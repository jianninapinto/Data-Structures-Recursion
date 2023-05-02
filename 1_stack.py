
# Using Python's deque module, implement a stack.


from collections import deque

class stack:
    def __init__(self):
        self.data = deque() # instantiate the deque class

    def push(self, value):
        # self.data.appendleft(value)
        self.data.append(value)

    def pop(self):
        return self.data.pop()
        # return self.data.popleft()

# Test cases:
myStack = stack()
myStack.push(3)
myStack.push(6)
myStack.push(9)
print(myStack.pop()) # 9
print(myStack.pop()) # 6
print(myStack.pop()) # 3

# Hint: push/pop operations in a stack happen on the same side. Picture a stack of pancakes -- adding and removing of flapjacks always happens from the "top" of the stack. With deque, we can use visualize either the "left" or "right" side of the double-ended queue as the "top" of the stack, so there are two ways to implement this.

# Useful built-in deque methods:
# append: add an element to the right side
# appendleft: add an element from the left side
# pop: add an element to the right side
# popleft: add an element from the left side