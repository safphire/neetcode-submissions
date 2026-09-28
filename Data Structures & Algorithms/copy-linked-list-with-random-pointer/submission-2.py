"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        storeNode = {}
        trav = head
        while trav:
            storeNode[trav] = Node(trav.val)
            trav = trav.next

        trav = head
        while trav:
            copy = storeNode[trav]
            copy.next = storeNode.get(trav.next)
            copy.random = storeNode.get(trav.random)
            trav = trav.next
        
        return storeNode[head]