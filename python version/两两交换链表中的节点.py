class Solution:
    def swap_nodes(self,head):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            node1 = node.next
            node2 = node.next.next
            node.next = node2
            node1.next = node2.next
            node2.next = node1
            node = node1
        return dummy.next
