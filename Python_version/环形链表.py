class Solution:
    def loop_list(self,head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        if not fast or not fast.next:
            return False
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
