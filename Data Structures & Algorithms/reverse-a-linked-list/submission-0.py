
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This normally requires some sort of dummy
        # the optimal solution will not convert to an array and back again

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        