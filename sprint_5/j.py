import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def __str__(self):
            return f'Node({self.value})'


def _insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key)
        else:
            _insert(root.left, key)
    else:
        if root.right is None:
            root.right = Node(value=key)
        else:
            _insert(root.right, key)


def insert(root, key) -> Node:
    _insert(root, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6

    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 7)
    assert node3.right.left.right.value == 7


if __name__ == '__main__':
    test()
