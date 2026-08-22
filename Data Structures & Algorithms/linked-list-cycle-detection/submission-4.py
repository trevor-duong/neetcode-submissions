# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node, fast_node = head, head
        while fast_node:
            slow_node = slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                break
            
            if slow_node == fast_node:
                return True
        return False