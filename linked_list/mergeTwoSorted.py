from linkedList import LinkedList, Node 
class Solution:
    def __init__(self) -> None:
        self.list1 = LinkedList([1,2,4])   
        self.list2 = LinkedList([1,3,4])   
    def mergeTwoLists(self):
        head = Node(None)
        merge = head 
        list1 = self.list1.head
        list2 = self.list2.head

        while list1 and list2:
            if list1.value <= list2.value:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
        merge = merge.next

        if list1:
            merge.next = list1
        elif list2:
            merge.next = list2

        print(head.next)
s = Solution()
s.mergeTwoLists()
