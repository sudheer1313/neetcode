class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.hashmap = {}

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            self.hashmap[val] = (None,self.head)
            return
        temp = self.tail
        newnode = Node(val)
        temp.next = newnode
        newnode.prev = temp
        self.tail = newnode
        self.hashmap[val] = (temp, newnode)

    def delete(self, val):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
            del self.hashmap[val]
            return
        if val in self.hashmap:
            prev, cur = self.hashmap[val]
            prev.next = cur.next
            cur.next.prev = prev
            del self.hashmap[val]
            return
        print(f"{val} is not existed in the linked list")




    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def dis_reverse(self):
        temp = self.tail
        while temp:
            print(temp.value, end=" ")
            temp = temp.prev


obj1 = Dll()
obj1.insert(20)
obj1.insert(30)
obj1.insert(40)
obj1.delete(20)
obj1.display()
obj1.dis_reverse()





