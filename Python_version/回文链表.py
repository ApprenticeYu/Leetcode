class Solution:
    def is_palindrome(self,head):
        if head is None:
            return True
        first_end = first_end_core(head)
        second_end = second_end_core(first_end.next)
        node = head
        find = True
        second_position = second_end
        while find and second_position:
            if node.val != second_position.val:
                find = False
                first_end.next = self.second_end_core(second_end)
                return find
            node = node.next
            second_position = second_position.next
        first_end.next = self.second_end_core(second_end)
        return find

    def first_end_core(self,head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def second_end_core(self,head):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
