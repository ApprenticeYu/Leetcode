class Solution:
    def reconnect(self,head):
        if not head:
            return
        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next
        i = 0
        j = len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None
