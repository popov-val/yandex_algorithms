from typing import Optional


class Node:
    def __init__(self, value, prev_val=None, next_val=None):
        self.value = value
        self.prev_val = prev_val
        self.next_val = next_val

    def __str__(self):
        return f'Node({self.value})'


class Queue:
    def __init__(self):
        self.queue: Optional[Node] = None
        self._size = 0

    def __str__(self):
        return f'Queue({str(self.queue)})'

    def put(self, el):
        put_node = Node(el)
        if not self.queue:
            self.queue = put_node
            self.queue.prev_val = put_node
            self.queue.next_val = put_node
        else:
            put_node.next_val = self.queue
            put_node.prev_val = self.queue.prev_val
            self.queue.prev_val = put_node
        self._size += 1

    def get(self):
        if not self.queue:
            print('error')
            return
        get_node = self.queue.value
        self.queue = self.queue.next_val
        self._size -= 1
        return get_node

    def size(self):
        return self._size


if __name__ == '__main__':
    # n = int(input())

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # for _ in range(n):
    #     command, *args = input().split()
    #     if args:
    #         args = [int(el) for el in args]
    #     method = getattr(q, command)
    #     output = method(*args)
    #     if output is not None:
    #         print(output)
