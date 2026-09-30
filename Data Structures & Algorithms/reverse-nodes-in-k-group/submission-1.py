# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(root):
            prev = None
            curr = root
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        

        dummyhead = ListNode(0, head)
        prevGroup = dummyhead

        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummyhead.next
                
            groupStart = prevGroup.next
            nextGroup = kth.next

            kth.next = None

            newHead = reverseList(groupStart)

            prevGroup.next = newHead
            groupStart.next = nextGroup

            prevGroup = groupStart
