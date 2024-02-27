class MyCircularDeque:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.elements = [0] * (k + 1)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % len(self.elements)
        self.elements[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % len(self.elements)
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front
