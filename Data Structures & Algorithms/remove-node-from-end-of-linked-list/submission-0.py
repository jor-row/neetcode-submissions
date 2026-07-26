# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0)
        slow = res
        fast = head

        i = 0

        while i < n:
            fast = fast.next
            i += 1

        while fast:
            print(head.val)
            slow.next = ListNode(head.val)
            head = head.next
            slow = slow.next
            fast = fast.next

        i = 0

        while head:
            if i > 0:
                slow.next = ListNode(head.val)
                slow = slow.next
            head = head.next
            i += 1

        return res.next
        