class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Insert at the beginning
def insertAtBeginning(head, val):
    newNode = ListNode(val)
    newNode.next = head
    return newNode

# Insert at the end
def insertAtEnd(head, val):
    newNode = ListNode(val)
    if not head:
        return newNode
    current = head
    while current.next:
        current = current.next
    current.next = newNode
    return head

# Insert at a specific pos
def insertAtPos(head, val, pos):
    newNode = ListNode(val)
    if pos == 0:
        newNode.next = head
        return newNode
    current = head
    for _ in range(pos - 1):
        current = current.next
        if not current:
            return head
    newNode.next = current.next
    current.next = newNode
    return head

# Function to print the list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("NULL")

# Example Usage
if __name__ == "__main__":
    head = None
    head = insertAtBeginning(head, 0)  # Insert 0 at beginning
    head = insertAtEnd(head, 1)  # Insert 1 at end
    head = insertAtPos(head, 2, 1)  # Insert 2 at pos 1

    print("Final Linked List:")
    printLinkedList(head)  # Output: 0 -> 2 -> 1 -> NULL
