import random

def generator(size, start, end):
    count = 0
    while count != (size):
        count += 1
        yield random.randint(start, end)


class Iterator:

    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        while self.length > 0:
            self.length -= 1
            return random.randint(self.start, self.end)
        if self.count == self.length:
            raise StopIteration

