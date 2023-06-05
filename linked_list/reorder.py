from linkedList import LinkedList, Node

class Solution:
    def __init__(self):
        self.list = LinkedList([1,2,3,4])

    def reorderList(self):
        head = self.list.head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        
        # reverse 2nd half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        print(self.list)


s = Solution()
print(s.reorderList())
