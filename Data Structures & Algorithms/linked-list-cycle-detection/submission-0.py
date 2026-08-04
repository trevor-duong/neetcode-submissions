# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# What condition can be checked to determine if there is a cycle?
# Naive is to keep track of visited nodes with a set
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        seen = set()
        while curNode:
            if curNode in seen:
                return True
            else:
                seen.add(curNode)
            curNode = curNode.next

        return False
            
