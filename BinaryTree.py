from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if self.root is None:
            newnode = Node(val)
            self.root = newnode
            return
        newnode = Node(val)
        q=deque([self.root])
        while q:
            node = q.popleft()
            if node.left is None:
                node.left = newnode
                return
            else:
                q.append(node.left)

            if node.right is None:
                node.right=newnode
                return
            else:
                q.append(node.right)

    def inorder(self,root):
        if  root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
    def preorder(self,root):
        if  root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if  root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value)




obj1=BinaryTree()
obj1.insert(10)
obj1.insert(20)
obj1.insert(30)
obj1.insert(40)
obj1.insert(50)
print("Inorder :")
obj1.inorder(obj1.root)
print("preorder :")
obj1.preorder(obj1.root)
print("postorder :")
obj1.postorder(obj1.root)





