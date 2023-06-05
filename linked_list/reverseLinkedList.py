from linkedList import LinkedList, Node

class Reverse:
    def __init__(self) -> None:
        self.linkedlist = LinkedList()
        self.linkedlist.add_node(Node(1))
        self.linkedlist.add_node(Node(2))
        self.linkedlist.add_node(Node(3))
        self.linkedlist.add_node(Node(4))
        self.linkedlist.add_node(Node(5))
    def reverseList(self):
        prev = Node(None)
        ll = self.linkedlist
        while ll.head:
            curr = ll.head.next
            ll.head.next = prev
            prev = ll.head
            ll.head = curr
        
        while prev:
            print(prev.value)
            prev = prev.next
r = Reverse()
r.reverseList()
