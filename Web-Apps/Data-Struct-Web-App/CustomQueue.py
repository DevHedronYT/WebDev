class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def Enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return
        
        self.tail.nextNode = Node(data, None)
        self.tail = self.tail.nextNode
        return 


    def Dequeue(self):
        if self.head is None:
            return None

        removed = self.head 
        self.head = self.head.nextNode
        
        if self.head is None:
            self.tail = None

        return removed

