# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        values=[]
        for head in lists:
            while head:
                values.append(head.val)
                head=head.next
        values.sort()
        dummy=ListNode()
        curr=dummy
        for i in values:
            curr.next=ListNode(i)
            curr= curr.next
        return dummy.next