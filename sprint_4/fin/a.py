from collections import defaultdict


def get_search_index(doc_list):
    search_index = defaultdict(lambda: defaultdict(int))
    for doc_num, doc in enumerate(doc_list):
        for word in doc.split():
            search_index[word][doc_num] += 1

    return search_index


def get_relevants(search_index, request, cnt_doc_rows):
    relevants = [[i, 0] for i in range(1, cnt_doc_rows + 1)]
    for word in set(request.split()):
        values = search_index.get(word, {})
        for doc_num, value in values.items():
            relevants[doc_num][1] += value
    return relevants


if __name__ == '__main__':
    cnt_doc_rows = int(input())
    doc_list = (input() for _ in range(cnt_doc_rows))
    search_index = get_search_index(doc_list)

    cnt_requests_rows = int(input())
    requests = (input() for _ in range(cnt_requests_rows))
    for request in requests:
        relevants = get_relevants(search_index, request, cnt_doc_rows)
        relevants.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        for i, [doc_num, relevant] in enumerate(relevants):
            if i > 4 or relevant == 0:
                print()
                break
            print(doc_num, end=' ')
