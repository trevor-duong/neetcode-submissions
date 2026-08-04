# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using a fast/slow pointer approach, both pointers will enter a cycle eventually and converge
        slowNode = fastNode = head 
        
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
            if slowNode == fastNode:
                return True

        return False