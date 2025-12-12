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
            return(self.list.pop())
        else:
            print("not enough items")
    def top(self):
        print(self.list[-1])
    def display(self):
        print(self.list)
    def size2(self):
        return(len(self.list))
#scan from left to right
#if an operant or operator is found move on to the next item in the expression
#if opening brackets are found then add it into the stack
#if a closing bracket is found then pop the top item of the stack and cheak if they are matching
#if they are not matching then print unbalenced expression
#repeat until end of expression
#if there is nothing un the stack then print balenced expression
list1 = ["(","[","{"]
list2 = [")","]","}"]
checker = Stack(20)
expression = "((2*3)"
for item in expression:
    print(item)
    if item in list1:
       checker.push(item)
    elif item in list2:
        pop_item = checker.pop()
        open_index = list1.index(pop_item)
        closed_index = list2.index(item)
        if open_index == closed_index:
            pass
        else:
            print("unbalanced")
            break
num = checker.size2()
if num==0:
    print("balenced")
else:
    print("unbalenced")

        
