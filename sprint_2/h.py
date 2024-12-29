class Stack:
    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        if not self.items:
            return
        self.items.pop()

    def top(self):
        if not self.items:
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Stack({self.items})'


brackets = {
    '}': '{',
    ')': '(',
    ']': '[',
}


def check_bracket(bk_close, bk_open):
    if brackets.get(bk_close) == bk_open:
        return True


if __name__ == '__main__':
    s = input()
    a = Stack()
    for el in s:
        if a.size() == 0:
            a.push(el)
        elif check_bracket(el, a.top()):
            a.pop()
        else:
            a.push(el)
    print(a.size() == 0)
