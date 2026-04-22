class NodeList:
    def __init__(self, val = 1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = NodeList(-1)
        self.tail = NodeList(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return True if self.head.next == self.tail else False

    def append(self, value: int) -> None:
        new_node = NodeList(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = NodeList(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
    
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.val
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value
    
    def popleft(self) -> int:
      if self.isEmpty():
        return -1
      value = self.head.next.val
      self.head.next = self.head.next.next
      self.head.next.prev = self.head
      return value