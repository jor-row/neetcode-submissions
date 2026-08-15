# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []

        while list1:
            arr1.append(list1.val)
            list1 = list1.next

        arr2 = []

        while list2:
            arr2.append(list2.val)
            list2 = list2.next

        res = arr1 + arr2
        res.sort()

        dummy = ListNode(0)
        curr = dummy

        for num in res:
            nxt = ListNode(num)
            curr.next = nxt
            curr = curr.next

        return dummy.next

        
        