import collections


class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = collections.deque(maxlen=k)

    def insert_front(self, value: int) -> bool:
        return len(self.queue) < self.queue.maxlen and (self.queue.appendleft(value) or True)

    def insert_last(self, value: int) -> bool:
        return len(self.queue) < self.queue.maxlen and (self.queue.append(value) or True)

    def delete_front(self) -> bool:
        return self.queue and (self.queue.popleft() or True)

    def delete_last(self) -> bool:
        return self.queue and (self.queue.pop() or True)

    def get_front(self) -> int:
        return not self.queue and -1 or self.queue[0]

    def get_rear(self) -> int:
        return not self.queue and -1 or self.queue[-1]

    def is_empty(self) -> bool:
        return not self.queue

    def is_full(self) -> bool:
        return len(self.queue) == self.queue.maxlen
