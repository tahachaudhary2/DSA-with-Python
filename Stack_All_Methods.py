class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def display(self):
        print(f"Current Stack is{self.items}")
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items)==0


s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())
print(s.peek())
print(s.is_empty())
