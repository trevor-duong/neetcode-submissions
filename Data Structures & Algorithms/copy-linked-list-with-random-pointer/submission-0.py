"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create bare deep copy of nodes + map from original node to new node
        translation_map = {}
        cur_node = head
        while cur_node:
            new_node = Node(x = cur_node.val)
            translation_map[cur_node] = new_node
            cur_node = cur_node.next
        # Edge case for when cur_node.next == random
        translation_map[None] = None

        cur_node = head
        while cur_node:
            # set new random to corresponding translated random
            translation_map[cur_node].random = translation_map[cur_node.random] 
            # set new next to corresponding translated next
            translation_map[cur_node].next = translation_map[cur_node.next]
            cur_node = cur_node.next
        return translation_map[head]
        