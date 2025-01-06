class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Sll:

    def __init__(self):
        self.head = None
        self.tail=None
        self.hashmap = {}

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            self.hashmap[val] = [(None, self.head)]
            return
        node = Node(val)
        self.tail.next = node
        temp = self.tail
        self.tail = node
        if val in self.hashmap:
            self.hashmap[val].append((temp, node))
        else:
            self.hashmap[val] = [(temp, node)]

    def delete(self, val, pos):
        if self.head is None:
            print("The linked list is empty")
            return
        if val in self.hashmap:
            if pos < len(self.hashmap[val]):
                prev, cur = self.hashmap[val][pos]
                if cur == self.head:
                    self.head = self.head.next
                else:
                    prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                del self.hashmap[val][pos]
            else:
                print("The position is out of range")
                return
        else:
            print(f"{val} is not found")


    def display(self):
        if self.head is None:
            print("Empty\n")

        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print("\n")
        print(self.hashmap)


obj1 = Sll()
obj1.insert(10)
obj1.insert(10)
obj1.insert(10)

obj1.insert(20)
obj1.insert(30)
obj1.insert(40)
obj1.delete(10, 0)
obj1.delete(10, 0)
obj1.delete(10, 0)
obj1.insert(10)
obj1.delete(80, 0)








obj1.display()
