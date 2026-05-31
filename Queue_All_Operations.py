class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Stack is Empty"
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items)==0
    def display(self):
        print(f"Current Queue is{self.items}")

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
print(q.peek())
print(q.is_empty())
q.display()
    