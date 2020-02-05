class LinearQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.queue = [None] * capacity

    def put(self, value):
        if self.is_full:
            """앞에 공간이 남아있지만,
            후단이 맨 뒤에 위치해 있으므로 오류 발생"""
            raise OverflowError('Overflow')

        self.queue[self.rear] = value
        self.rear += 1

    def get(self):
        if self.is_empty:
            raise Exception('Underflow')

        value = self.queue[self.front]
        self.front += 1
        return value

    @property
    def is_empty(self):
        return self.front == self.rear

    @property
    def is_full(self):
        return (
            False if self.is_empty
            else self.rear == self.capacity
        )
