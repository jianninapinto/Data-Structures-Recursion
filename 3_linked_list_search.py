# Convert it to a recursive solution, i.e., the search function must call itself instead of using a loop.


class listNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# def search(head, value):
#     current = head
#     while(current is not None): # until we have reached the tail
#         if(current.value == value): # if we find the given value
#             return True
#         current = current.next # if we did not find the given value
#     return False

def search(head, value):
    # Base case
    if (head is None):
        return False
    # If we find the given value (value exists)
    elif (head.value == value):
        return True
    # If we did not find the object we move to the next node
    else:
        return search(head.next, value) # recursive case


# This function searches a linked list built from the provided listNode class, returning True if an element is found in the linked list. It returns False otherwise.

# Hint: what is the base case?



# Test cases:
head = listNode(3)
head.next = listNode(6)
head.next.next = listNode(9)
# The linked list is 3 -> 6 -> 9 (3 is the head of the list)

print(search(head, 3)) # True
print(search(head, 0)) # False
print(search(head, 9)) # True