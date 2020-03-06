class CircularQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity + 1
        self.front = 0
        self.rear = 0
        self.queue = [None] * capacity

    def put(self, value) -> None:
        if self.is_full:
            raise OverflowError
        self.queue[self.rear] = value
        self.rear += 1
        if self.capacity == self.rear:
            self.rear = 0

    def get(self):
        if self.is_empty:
            raise Exception
        value = self.queue[self.front]
        self.front += 1
        if self.capacity == self.front:
            self.front = 0
        return value

    @property
    def is_empty(self) -> bool:
        return self.front == self.rear

    @property
    def is_full(self) -> bool:
        return (
            False if self.is_empty
            else (self.rear + 1) == (self.front + self.capacity)
        )
