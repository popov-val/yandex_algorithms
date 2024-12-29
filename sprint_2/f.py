import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.items:
            sys.stdout.write('error')
            sys.stdout.write('\n')
            return
        self.items.pop()

    def get_max(self):
        if not self.items:
            sys.stdout.write('None')
            sys.stdout.write('\n')
            return
        return max(self.items)


if __name__ == '__main__':
    n = sys.stdin.readline()

    a = Stack()
    for _ in range(int(n)):
        command, *args = sys.stdin.readline().rstrip().split()
        if args:
            args = [int(el) for el in args]
        method = getattr(a, command)
        output = method(*args)
        if output is not None:
            sys.stdout.write(str(output))
            sys.stdout.write('\n')
