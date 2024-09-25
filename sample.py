class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value stored in the node
        self.next = next  # Pointer to the next node


# Create individual nodes
node1 = ListNode(1)  # Node with value 1
node2 = ListNode(2)  # Node with value 2
node3 = ListNode(3)  # Node with value 3

# Link the nodes together
node1.next = node2  # Node1 points to Node2
node2.next = node3  # Node2 points to Node3

# At this point, we have a linked list: 1 -> 2 -> 3 -> NULL
def print_linked_list(head):
    current = head  # Start from the head of the list
    while current:
        print(current.val, end=" -> ")  # Print the value of the current node
        current = current.next  # Move to the next node
    # print("NULL")  # Indicate the end of the list

# Example usage:
print_linked_list(node1)  # Output: 1 -> 2 -> 3 -> NULL
