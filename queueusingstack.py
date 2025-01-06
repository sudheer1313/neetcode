#queueusingstack.py
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def Enqueue(self,val):
        if self.head is None:
            self.head=Node(val)
            print(f"{val} is enqueued")
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        newnode=Node(val)
        temp.next=newnode
        print(f"{val} is enqueued")
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
            return
        val=self.head.value
        self.head=self.head.next
        print(f"the dequeue element is {val}")
    def peek(self):
        if self.head is None:
            print("queue is empty")
            return
        val=self.head.value
        print(f"the peek element is {val}")
    def display(self):
        if self.head is None:
            print("queue is empty")
            return
        cur=self.head
        while cur:
            print(cur.value,end=" ")
            cur=cur.next

obj1=Queue()
obj1.Enqueue(10)
obj1.Enqueue(13)
obj1.Enqueue(1)
obj1.Enqueue(20)
obj1.dequeue()
obj1.peek()
obj1.display()

