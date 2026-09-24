# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPtr = head
        slowPtr = head
        while fastPtr and fastPtr.next != None:
            slowPtr = slowPtr.next
            if fastPtr.next:
                fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True
        return False