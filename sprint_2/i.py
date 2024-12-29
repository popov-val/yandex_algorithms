class Queue:
    def __init__(self, n):
        self.max_size = n
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, el):
        if self.size() == self.max_size:
            print('error')
            return
        self.queue[self.tail] = el
        self.tail = (self.tail + 1) % self.max_size
        self.queue_size += 1

    def pop(self):
        if self.size() == 0:
            print('None')
            return
        el = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return el

    def peek(self):
        if self.size() == 0:
            print('None')
            return
        return self.queue[self.head]

    def size(self):
        return self.queue_size

    def __str__(self):
        return f'Queue({str(self.queue)})'


if __name__ == '__main__':
    n = int(input())
    size = int(input())
    q = Queue(size)
    for _ in range(n):
        command, *args = input().split()
        if args:
            args = [int(el) for el in args]
        method = getattr(q, command)
        output = method(*args)
        if output is not None:
            print(output)
