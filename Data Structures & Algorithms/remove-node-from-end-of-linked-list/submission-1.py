# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)

        # Priming loop, setting second pointer to n+1 ahead of slow 
        # (+1 because we want to be 1 before the nth node, as to 
        # reassign pointers)
        first, second = dummy, dummy
        for i in range(n+1):
            second = second.next
        
        # advance both first and second to end of list
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return dummy.next


