
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        cur = self.head
        for i in range(index):
            if cur is None:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def addAtHead(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        new = Node(val)
        new.next = cur.next
        cur.next = new

    def deleteAtIndex(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next
