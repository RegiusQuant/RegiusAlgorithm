class ListNode:

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1

        node = self.table[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            node = ListNode(key, value)
            self.table[key] = node
            self.insert(node)
            if len(self.table) > self.capacity:
                del self.table[self.tail.prev.key]
                self.remove(self.tail.prev)
        else:
            node = self.table[key]
            node.value = value
            self.remove(node)
            self.insert(node)

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: ListNode) -> None:
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
