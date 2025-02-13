def sift_up(heap, idx) -> int:
    head_idx = idx // 2
    if heap[head_idx] > heap[idx] or idx == 1:
        return idx
    heap[head_idx], heap[idx] = heap[idx], heap[head_idx]
    return sift_up(heap, head_idx)


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
