# ChatGPT

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode()  # Create a dummy head node
    current = dummy     # Current node pointer

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # If there are remaining nodes, connect them to the end of the merged list
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next  # Return the head node of the merged list


# Example
# Create linked list 1 -> 2 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))

# Create linked list 1 -> 3 -> 4
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = mergeTwoLists(l1, l2)  # Merge two sorted lists
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
