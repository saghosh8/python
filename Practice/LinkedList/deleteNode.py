class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Delete the first node
def delete_first_node(head):
    if head is None:
        return None
    return head.next

# Delete the last node
def delete_last_node(head):
    if head is None or head.next is None:
        return None
    
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    return head

# Delete at a specific position
def delete_at_position(head, position):
    if head is None:
        return None
    
    if position == 0:
        return head.next

    current = head
    for _ in range(position - 1):
        if current.next is None:
            return head
        current = current.next

    if current.next is not None:
        current.next = current.next.next

    return head

# Function to print the list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("NULL")

# Example usage
if __name__ == "__main__":
    # Create a simple linked list 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print("Original Linked List:")
    print_linked_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> NULL

    # Delete the first node
    head = delete_first_node(head)
    print("After Deleting First Node:")
    print_linked_list(head)  # Output: 2 -> 3 -> 4 -> NULL

    # Delete the last node
    head = delete_last_node(head)
    print("After Deleting Last Node:")
    print_linked_list(head)  # Output: 2 -> 3 -> NULL

    # Delete node at position 1
    head = delete_at_position(head, 1)
    print("After Deleting Node at Position 1:")
    print_linked_list(head)  # Output: 2 -> NULL
