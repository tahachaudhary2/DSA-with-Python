class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left= insert(root.left,key)
    elif key>root.data:
        root.right= insert(root.right,key)
    return root
def search(root,key):
    if root is None or root.data==key:
        return root
    if key<root.data:
        return search(root.left,key)
    return search(root.right,key)        


root=None
values=[10,32,21,1,4,5,66,15]
for v in values:
    root=insert(root,v)
print("Seach for 21:","Found" if search(root,21) else "Not Found")
print("Search for 99:","Found" if search(root,99) else "Not Found")