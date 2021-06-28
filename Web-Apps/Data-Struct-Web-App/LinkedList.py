class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def ToArray(self):
        arr = []

        if self.head is None:
            return arr

        node = self.head
        while node:
            arr.append(node.data)
            node = node.nextNode

        return arr
    
    def PrintLL(self): 
        llString = ""
        node = self.head

        if node is None:
            print(None)

        while node:
            llString += f"{str(node.data)} -> "
            node = node.nextNode

        llString += "None"
        print(llString)


    def InsertBeginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.lastNode = self.head
            return 

        newNode = Node(data, self.head)
        self.head = newNode

    def InsertEnd(self, data):
        if self.head is None:
            self.InsertBeginning(data)
            return

        self.lastNode.nextNode = Node(data, None)
        self.lastNode = self.lastNode.nextNode


    def GetUserByID(self, ID):
        node = self.head
        while node:
            if node.data["id"] is int(ID):
                return node.data

            node = node.nextNode
        return None

