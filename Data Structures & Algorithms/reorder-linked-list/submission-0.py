# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeStore = [head]
        nav = head
        nav = nav.next
        while nav:
            nodeStore.append(nav)
            nav = nav.next
        l, r = 0 , len(nodeStore) - 1
        while l < r:
            nodeStore[l].next = nodeStore[r]
            l += 1
            if l == r:
                break
            nodeStore[r].next = nodeStore[l]
            r -= 1
        nodeStore[l].next = None