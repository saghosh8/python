class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
beg = ListNode(0)

node1.next = node2
node2.next = node3


def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("Null")

printList(node1)
