class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


class Stack:
    def __init__(self):
        self.top = None

    def Peek(self):
        return self.top

    def Push(self, data):
        nextNode = self.top
        self.top = Node(data, nextNode)

    def Pop(self):
        if self.top is None:
            return None

        removed = self.top
        self.top = self.top.nextNode
        return removed


