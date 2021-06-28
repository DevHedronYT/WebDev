class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
class HashTable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [None] * tableSize

    def Hash(self, key):
        hashVal = 0
        for i in key:
            hashVal += ord(i)
            hashVal = (hashVal * ord(i)) % self.tableSize

        return hashVal

    def AddKeyVal(self, key, value):
        hashedKey = self.Hash(key)
        if self.hashTable[hashedKey] is None:
            self.hashTable[hashedKey] = Node(Data(key, value), None)

        else:
            node = self.hashTable[hashedKey]
            while node.nextNode:
                node = node.nextNode

            node.nextNode = Node(Data(key, value), None)

    def GetVal(self, key):
        hashedKey = self.Hash(key)
        if self.hashTable[hashedKey] is not None:
            node = self.hashTable[hashedKey]
            if node.nextNode is None:
                return node.data.value

            while node.nextNode:
                if key == node.data.key:
                    return node.data.value

                node = node.nextNode

            if key == node.data.key:
                return node.data.value

        return None

    def PrintTable(self):
        print("{")
        for i, val in enumerate(self.hashTable):
            if val is not None:
                llistS = ""
                node = val
                if node.nextNode:
                    while node.nextNode:
                        llistS += (str(node.data.key) + " : " + str(node.data.value) + " --> ")
                        node = node.nextNode

                    llistS += (str(node.data.key) + " : " + str(node.data.value) + " --> None")
                    print(f"   [{i}] {llistS}")

                else:
                    print(f"   [{i}] {val.data.key} : {val.data.value}")

            else:
                print(f"   [{i}] {val}")

        print("}")
                    

