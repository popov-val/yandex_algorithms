def sift_down(heap, idx) -> int:
    child_left = idx * 2
    child_right = idx * 2 + 1
    if child_left >= len(heap):
        return idx
    if child_right >= len(heap):
        max_el = max(heap[idx], heap[child_left])
    else:
        max_el = max(heap[idx], heap[child_left], heap[child_right])
    if heap[idx] == max_el:
        return idx
    if heap[child_left] == max_el:
        heap[child_left], heap[idx] = heap[idx], heap[child_left]
        return sift_down(heap, child_left)
    if heap[child_right] == max_el:
        heap[child_right], heap[idx] = heap[idx], heap[child_right]
        return sift_down(heap, child_right)


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5

    sample = [0, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5

    sample = [0, 10, 1, 8, 3, 4, 7]
    assert sift_down(sample, 1) == 1

    sample = [0, 11, 9, 6, 2, 4, 1]
    assert sift_down(sample, 1) == 1

    sample = [0, 0, 9, 6, 2, 4, 1]
    assert sift_down(sample, 1) == 5

    # - - -
    sample = [0, -4, 9, 6, 2, 4, 1]
    assert sift_down(sample, 1) == 5

    sample = [0, -4, 9, 0, 2, 4, 1]
    assert sift_down(sample, 3) == 6

    sample = [0, -4, 1, 0, 2, 4, 1]
    assert sift_down(sample, 2) == 5

    sample = [0, -4, -3, 0, 2, 4, 1]
    assert sift_down(sample, 2) == 5

    sample = [0, -4, -3, 0, 2, 4, -9]
    assert sift_down(sample, 6) == 6

    sample = [0, -4, -3, 0, 2, 3, -9]
    assert sift_down(sample, 5) == 5


if __name__ == '__main__':
    test()
