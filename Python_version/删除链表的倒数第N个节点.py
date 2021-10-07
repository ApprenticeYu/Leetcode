class Solution:
    def the_reverse_node(self,head,n):
        if not head:
            return list()
        dummy = ListNode(0,head)
        first = dummy
        second = head
        for i in range(n):
            second = second.mext
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
