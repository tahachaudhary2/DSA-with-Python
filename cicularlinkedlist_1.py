class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circularlinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
    def display(self):
        if not self.head:
            print("List is Empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("Back to head")

cll=Circularlinkedlist()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()
