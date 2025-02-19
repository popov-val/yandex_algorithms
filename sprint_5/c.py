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
        return res
    if root.left is not None:
        res.extend(go_left(root.left))
    res.append(root.value)
    if root.right is not None:
        res.extend(go_left(root.right))
    return res


def go_right(root):
    res = []
    if root is None:
        return res
    if root.right is not None:
        res.extend(go_right(root.right))
    res.append(root.value)
    if root.left is not None:
        res.extend(go_right(root.left))
    return res


def solution(root) -> bool:
    left = go_left(root.left)
    right = go_right(root.right)
    return left == right


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)

    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node2, node1)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert not solution(node7)

    node8 = Node(0)
    node7 = Node(1)
    node6 = Node(1)
    node5 = Node(0)
    node4 = Node(3, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, right=node4)
    node1 = Node(2, node3)
    node0 = Node(0, node1, node2)
    assert solution(node0)


if __name__ == '__main__':
    test()
