class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def print(self):
        print(f"Current Stack is {self.items}")

s=Stack()
for i in range(3):
    num=int(input("Enter Your Number: "))
    s.push(num)


s.print()
