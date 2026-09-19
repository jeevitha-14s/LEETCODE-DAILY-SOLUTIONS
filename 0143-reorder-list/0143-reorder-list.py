class Solution:
        def reorderList(self, head) -> None:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            prev = None
            while second:
                nxt = second.next
                second.next = prev
                prev = second
                second = nxt
            first = head
            while prev:
                f2 = first.next
                p2 = prev.next
                first.next = prev
                prev.next = f2
                first = f2
                prev = p2