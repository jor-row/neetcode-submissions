# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        arr = arr[::-1]

        dummy= ListNode(0)
        curr = dummy

        for num in arr:
            n = ListNode(num)
            curr.next = n
            curr = curr.next

        return dummy.next
        