# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # def printval(t):
        #     while t:
        #         print(t.val)
        #         t = t.next

        t1, t2 = l1, l2
        prev = None
        carry = 0
        while t1 and t2:
            val = t1.val + t2.val + carry
            t1.val = val % 10
            carry = val // 10
            prev = t1
            t1 = t1.next
            t2 = t2.next

        if t2:
            prev.next = t2
        t1 = prev.next
        while t1:
            val = t1.val + carry
            t1.val = val % 10
            carry = val // 10
            t1 = t1.next
        if carry:
            t1 = l1
            while t1.next:
                t1 = t1.next
            t1.next = ListNode(1)
        # printval(l1)
        return l1

        