def insert_at_beginning(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
def delete(self,target):
    if not self.head:
        print("List is Empty,nothing to print fuck off !!")
        return
    if self.head.data==target:
        self.head=self.head.next
        return
    temp=self.head
    while temp.next:
        if temp.next.data==target:
            temp.next=temp.next.next
            return
        temp=temp.next
    print(f"{target} not found")