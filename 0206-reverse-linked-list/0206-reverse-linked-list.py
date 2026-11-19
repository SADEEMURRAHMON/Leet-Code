class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("NULL")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Before Reverse:")
print_list(head)

new_head = Solution().reverseList(head)

print("After Reverse:")
print_list(new_head)