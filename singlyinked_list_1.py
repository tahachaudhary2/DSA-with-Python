class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class Linkedlist:
    def __init__(self):
        self.head= None
    def insert_at_end(self,data):
        new_node= Node(data)
        if not self.head:
            self.head= new_node
            return
        temp= self.head
        while temp.next:
            temp=temp.next
        temp.next= new_node
    def display(self):
        if not self.head:
            print("List is Empty")
            return
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
    def search(self,target):
        temp= self.head
        while temp:
            if temp.data==target:
                return True
            temp=temp.next
        return False
    
ll=Linkedlist()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
print(ll.search(20))
print(ll.search(50))
            


        
        