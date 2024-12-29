

class Queue:
    def __init__(self):
        self.queue = []
        self._size = 0

    def __str__(self):
        return f'Queue({str(self.queue)})'

    def put(self, el):
        self.queue.append(el)
        self._size += 1

    def get(self):
        if not self.queue:
            print('error')
            return

        self._size -= 1
        return self.queue.pop(0)

    def size(self):
        return self._size


if __name__ == '__main__':
    n = int(input())

    q = Queue()

    for _ in range(n):
        command, *args = input().split()
        if args:
            args = [int(el) for el in args]
        method = getattr(q, command)
        output = method(*args)
        if output is not None:
            print(output)
