#StackusingLinkedList.py
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,val):
        if self.head is None:
            self.head=Node(val)
            print(f"{val} is pushed")
            return
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        print(f"{val} is pushed")
    def pop(self):
        if self.head is None:
            print("stack is empty")
            return
        val=self.head.value
        self.head=self.head.next
        print(f"the popped element is {val}")
    def peek(self):
        if self.head is None:
            print("stack is empty")
            return
        val=self.head.value
        print(f"The top most element of the stack is {val}")
    def display(self):
        cur=self.head
        while cur:
            print(cur.value,end=" ")
            cur=cur.next





obj1=Stack()
obj1.push(10)
obj1.push(20)
obj1.pop()
obj1.push(30)
obj1.push(13)
obj1.peek()
obj1.display()





