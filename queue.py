class queue:
    def __init__(self):
        self.s = []
    
    def enqueue(self, x):
        self.s.append(x)

    def dequeue(self):
        if len(self.s)>=1:
            self.s = self.s[1:]
        else:
            print("Queue is empty!")
    
    def show(self):
        print(self.s)

if __name__ == "__main__":
    q = queue()

    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(5)

    print("Queue after the enqueue operation : {}".format(q.show()))

    q.dequeue()
    print("Queue after the dequeue operation : {}".format(q.show()))
