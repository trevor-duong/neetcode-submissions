class Node:
    def __init__(self, key: int = -1, value: int = -1, next: 'Node' = None, prev: 'Node' = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node_map = {}
        self.capacity = capacity
        self.cur_capacity = 0

    def _remove(self, node: 'Node') -> None:
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

        if node.key in self.key_node_map:
            del self.key_node_map[node.key]
        
        self.cur_capacity -= 1

    def _insert_front(self, node:'Node'):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.key_node_map[node.key] = node

        self.cur_capacity += 1


    def get(self, key: int) -> int:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self._remove(node)
            self._insert_front(node = node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self._remove(node)
            self._insert_front(node)
        else: #key not in list
            if self.cur_capacity >= self.capacity:
                self._remove(self.tail.prev)
            new_node = Node(key = key, value = value)
            self._insert_front(new_node)