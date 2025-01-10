class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the head
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

    # Convert the linked list to a list of elements (for easier handling)
    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Stack Class
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack: ", " --> ".join(map(str, self.items)))

# Function to move elements from linked list to stack and pop in reverse
def reverse_linked_list_and_pop(linked_list):
    stack = Stack()
    
    # Push all elements from the linked list into the stack
    current = linked_list.head
    while current:
        stack.push(current.data)
        current = current.next
    
    # Now pop from the stack to get elements in reverse order
    print("Reversed List by popping from the stack:")
    while not stack.is_empty():
        print(stack.pop(), end=" --> ")
    print("None")  # End of the list

# Example usage:

# Creating a linked list
ll = LinkedList()
ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_end(40)
ll.insert_end(50)

# Printing the linked list
print("Original Linked List:")
ll.print_list()

# Reversing the linked list using stack
reverse_linked_list_and_pop(ll)
