class Stack:
    def __init__(self):
        self.items = []
        self._max_el = None

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.items:
            print('error')
            return
        self.items.pop()

    def top(self):
        if not self.items:
            print('error')
            return
        return self.items[-1]

    def get_max(self):
        if not self.items:
            print('None')
            return
        return max(self.items)


if __name__ == '__main__':
    n = int(input())

    a = Stack()
    for _ in range(n):
        command, *args = input().split()
        if args:
            args = [int(el) for el in args]
        method = getattr(a, command)
        output = method(*args)
        if output is not None:
            print(output)
