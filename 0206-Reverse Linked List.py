# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointer1 = head
        while pointer1 != None:
            pointer2 = pointer1.next
            pointer1.next = prev
            prev = pointer1
            pointer1 = pointer2
        return prev