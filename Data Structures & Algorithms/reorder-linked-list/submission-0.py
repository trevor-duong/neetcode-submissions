# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1 cut the list in half
        prev, slow, fast = head, head, head
        while fast:
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next            
            else:
                break
        
        # slow pointer pointing to middle index + 1 (beginning of second half)
        prev.next = None

        # Reverse second half
        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        # two lists, first head is head, second is at prev_node (reversed)


        while head and prev_node:
            head_next = head.next
            prev_next = prev_node.next
            head.next = prev_node
            prev_node.next = head_next
            head = head_next
            prev_node = prev_next
        
            