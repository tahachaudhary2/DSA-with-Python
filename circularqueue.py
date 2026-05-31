class circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def is_full(self):
        return (self.rear+1) % self.size==self.front
    def is_empty(self):
        return self.front==-1
    def  enqueue(self,data):
        if self.is_full():
            print("Queue is Full")
            return
        if self.is_empty():
            self.front=0
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data= self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front +1)%self.size
        return data
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        i= self.front
        while True:
            print(self.queue[i],end=" ")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print()

cq=circularqueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(50)
cq.enqueue(60)
cq.display()