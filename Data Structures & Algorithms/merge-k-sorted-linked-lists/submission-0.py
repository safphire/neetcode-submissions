# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(currentHead: ListNode, list2: ListNode):
            tempCurrentHead = currentHead
            while tempCurrentHead.next and list2:
                if tempCurrentHead.next.val > list2.val:
                    temp = tempCurrentHead.next
                    tempCurrentHead.next = list2
                    list2 = list2.next
                    tempCurrentHead.next.next = temp
                tempCurrentHead = tempCurrentHead.next
            if list2:
                print(tempCurrentHead)
                tempCurrentHead.next = list2


        if len(lists) < 1:
            return None
        
        currentHead = ListNode(-2000) # Initialize with value smaller than constraints
        i = 0
        while i < len(lists):
            merge(currentHead, lists[i])
            i += 1
        return currentHead.next