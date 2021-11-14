class Solution:
    def insert_sort(self,head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last_sort = head
        cur = last_sort.next
        while cur:
            if last_sort.value <= cur.value:
                last_sort = last_sort.next
            else:
                pre = dummy
                while pre.next.value <= cur.value:
                    pre = pre.next
                last_sort.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_sort.next
        return dummy.next
