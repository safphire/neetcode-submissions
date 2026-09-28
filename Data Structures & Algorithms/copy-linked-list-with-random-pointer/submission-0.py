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
        def createDeepCopy(root, storeNode):
            if not root:
                return None
            
            if root in storeNode:
                return storeNode[root]
            
            copy = Node(root.val)
            storeNode[root] = copy
            copy.next = createDeepCopy(root.next, storeNode)
            copy.random = createDeepCopy(root.random, storeNode)
            return copy
            
        # storeRandom = {}
        # trav = head
        # while trav:
        #     random = None
        #     copy = Node(trav.val, trav.next, random)
        #     if trav.random in storeRandom:
        #         random = storeRandom[trav.random]
        #     else:
        #         random = Node(trav.random.val, trav.random.next, None)
        #     storeRamdom[trav] = Node
        #     storeRandom
        # storeRandom[] = None
        # print(storeRandom)

        
        storeNode = {}
        return createDeepCopy(head, storeNode)