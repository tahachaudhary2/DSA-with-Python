class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(2)
root.left.right=Node(7)

def preorder(node):
    if node:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=" ")

print("Preorder Traversasl:")
preorder(root)

print("\nInorder Traversasl:")
inorder(root)

print("\nPostorder Traversasl:")
postorder(root)
