class Solution:
    def odd_even_list(self,head):
        if not head:
            return head
        even_head = head.next
        odd,even = head,even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
