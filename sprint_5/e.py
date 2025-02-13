import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def _solution(root, min_val=None, max_val=None):
    if root is None:
        return True

    if min_val is not None:
        if min_val >= root.value:
            return False

    if max_val is not None:
        if root.value >= max_val:
            return False

    left_flag = _solution(root.left, min_val, root.value)
    right_flag = _solution(root.right, root.value, max_val)

    return left_flag and right_flag


def solution(root) -> bool:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return _solution(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
