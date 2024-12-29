def main(n, m, matrix):
    t_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = [input().split() for i in range(n)]
    for row in main(n, m, matrix):
        print(*row)
