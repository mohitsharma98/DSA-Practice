class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printlinkedlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    l = Linked_List()
    l.insert(2)
    l.insert(4)
    l.insert(5)
    l.insert(7)
    l.printlinkedlist()