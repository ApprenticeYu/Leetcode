class Solution:
    def reverse_node(self,head,left,right):
        if not head or left > right:
            return None
        if left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = pre.next
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy.next
