# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create a reversed linked list, at some point we will reach the hinge of the palindrome, at which point
        # before we add the next val we will have reversed == next. if we don't get to that point and 
        # the linked list goes to null then false

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True

        # slow will now point to the mid point


        