class Stack:
    def __init__(self,size):
        self.size = size
        self.list = []
    def push(self,item): 
        if len(self.list)<self.size:
            self.list.append(item)
        else:
            print("not enough space")
    def pop(self):
        if len(self.list)>0:
            self.list.pop()
        else:
            print("not enough items")
    def top(self):
        print(self.list[-1])
    def display(self):
        print(self.list)
        
Stack1 = Stack(5)
Stack1.display()
Stack1.push(2)
Stack1.push(6)
Stack1.push(7)
Stack1.display()
Stack1.top()
Stack1.pop()
Stack1.pop()
Stack1.pop()
Stack1.pop()
Stack1.display()
Stack1.push(6)
Stack1.push(6)
Stack1.push(6)
Stack1.push(6)
Stack1.push(6)
Stack1.push(6)
Stack1.push(6)
