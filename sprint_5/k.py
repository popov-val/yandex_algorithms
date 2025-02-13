import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def __str__(self):
            return f'Node({self.value})'


def get_range(node, l, r, ):
    res = []

    if node.value >= l and node.left is not None:
        res.extend(get_range(node.left, l, r))

    if l <= node.value <= r:
        res.append(node.value)

    if node.value <= r and node.right is not None:
        res.extend(get_range(node.right, l, r))

    return res


def print_range(node, l, r):
    res = get_range(node, l, r)
    print(*res)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    assert print_range(node7, 2, 8) == [2, 5, 8, 8]
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
