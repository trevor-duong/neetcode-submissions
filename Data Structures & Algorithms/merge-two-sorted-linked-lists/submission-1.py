# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1, cur_l2 = list1, list2
        sentinel = ListNode()
        tail = sentinel

        while cur_l1 and cur_l2:
            if cur_l1.val <= cur_l2.val:
                tail.next = cur_l1
                cur_l1 = cur_l1.next
            else:
                tail.next = cur_l2
                cur_l2 = cur_l2.next
            tail = tail.next

        tail.next = cur_l1 if cur_l1 else cur_l2
        return sentinel.next
