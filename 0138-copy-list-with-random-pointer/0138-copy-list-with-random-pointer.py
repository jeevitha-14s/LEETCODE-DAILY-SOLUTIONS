class Solution:
        def copyRandomList(self, head):
            mapping = {None: None}
            nd = head
            while nd:
                mapping[nd] = Node(nd.val)
                nd = nd.next
            nd = head
            while nd:
                mapping[nd].next = mapping[nd.next]
                mapping[nd].random = mapping[nd.random]
                nd = nd.next
            return mapping[head]