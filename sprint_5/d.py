import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

        def __str__(self):
            return f'Node({self.value})'


def go_left(root):
    res = []
    if root is None:
        return [None]
    res.extend(go_left(root.left))
    res.append(root.value)
    res.extend(go_left(root.right))
    return res


def solution(root1, root2) -> bool:
    r_1 = go_left(root1)
    r_2 = go_left(root2)
    return r_1 == r_2


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()
