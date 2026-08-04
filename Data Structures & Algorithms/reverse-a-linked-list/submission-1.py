# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# as we iterate through the list we want to set the nextNodes.next -> curNode
# To move on though we need to keep track of 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastNode = None
        curNode = nextNode = head
        print(curNode, lastNode)
        while curNode:
            nextNode = curNode.next
            curNode.next = lastNode
            lastNode = curNode
            curNode = nextNode
        return lastNode
        