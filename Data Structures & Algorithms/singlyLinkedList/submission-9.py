class NodeList:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = NodeList()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = NodeList(val)
        curr = self.head.next
        new_node.next = curr
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = NodeList(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        list_vals = []
        curr = self.head.next
        while curr:
            list_vals.append(curr.val)
            curr = curr.next
        return list_vals
        
