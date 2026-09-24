class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        tempHead = self.head
        while tempHead != None:
            if i == index:
                return tempHead.val
            tempHead = tempHead.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        if self.head == None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            node = ListNode( val, self.head)
            self.head = node

    def insertTail(self, val: int) -> None:
        if self.tail == self.head == None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            node = ListNode(val)
            self.tail.next = node
            self.tail = node

    def remove(self, index: int) -> bool:
        # if self.head == None:
        #     return False
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = self.head
        #     return True
        # i = 0
        # tempHead = self.head
        # while i < index and tempHead != None:
        #     if i == index - 1:
        #         if tempHead.next == self.tail:
        #             self.tail = tempHead
        #         tempHead.next = tempHead.next.next
        #         return True
        #     i += 1
        # return False
        if index < 0 or self.head is None:
            return False

        # remove head
        if index == 0:
            self.head = self.head.next
            if self.head is None:   # list became empty
                self.tail = None
            return True

        # walk to node before index
        prev = self.head
        i = 0
        while prev is not None and i < index - 1:
            prev = prev.next
            i += 1

        if prev is None or prev.next is None:
            return False  # index out of bounds

        # remove node
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        tempHead = self.head
        res = []
        while tempHead != None:
            print (tempHead.val)
            res.append(tempHead.val)
            tempHead = tempHead.next
        return res
