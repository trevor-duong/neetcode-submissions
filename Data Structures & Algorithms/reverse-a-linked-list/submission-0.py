# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        lastNode = None
        while curNode != None:
            nextNode = curNode.next
            curNode.next = lastNode
            lastNode = curNode
            curNode = nextNode

        return lastNode