class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if len(self.s) >= 1:
            self.s = self.s[:-1]
        else:
            print("Array is already empty!")

    def top(self):
        if len(self.s) >= 1:
            return self.s[-1]
        else:
            print("Array is empty! Cannot return the top element!")

    def show(self):
        return self.s

if __name__ == "__main__":
    a = Stack()
    a.push(2)
    a.push(6)
    a.push(9)
    a.push(4)
    a.push(5)

    print("Current array elements : {}".format(a.show()))

    print("Current top element in the stack : {}".format(a.top()))

    

    a.pop()
    print("result after popping top element : {}".format(a.show()))

    print("New top element after popping in the stack : {}".format(a.top()))

    a.pop()
    a.pop()
    a.pop()
    a.pop()

    a.top()