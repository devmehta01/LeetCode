# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans==ans[::-1]



########## ANOTHER METHOD O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow, fast is None
        
        if not head or not head.next:
            return True
        
        mid, isEven = middle(head)

        if not isEven:
            mid.val = None
            mid = mid.next
        
        prev, curr = None, mid

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while head and head.val != None and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True