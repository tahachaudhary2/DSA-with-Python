class Dnode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Dnode(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def display_forward(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
    def display_backward(self):
        temp=self.head
        if not temp:
            print("List is Empty")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end="<->")
            temp=temp.prev
        print("None")


dll=Doublylinkedlist()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.display_forward()
dll.display_backward()
