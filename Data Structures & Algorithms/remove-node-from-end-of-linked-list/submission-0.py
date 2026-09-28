# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = 0
        slw = head
        fst = head
        while fst:
            fst = fst.next
            end += 1
        print (end - n)
        for i in range(end - n - 1):
            slw = slw.next
        
        if end == n:
            return head.next if head.next else None
        if slw.next and slw.next.next:
            slw.next = slw.next.next
        elif slw.next:
            slw.next = None
        return head