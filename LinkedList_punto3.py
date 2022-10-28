
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_d):
        new_node = Node(new_d)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(5)
llist.push(6)
llist.push(7)
llist.push(8)
llist.push(9)
llist.push(10)
llist.push(11)

print("Lista Enlazada")
llist.printList()
llist.reverse()
print("\nLista Enlazada Invertida")
llist.printList()
