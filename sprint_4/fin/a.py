def get_search_index(doc_list, doc_cnt):
    search_index = {}
    for doc_num, doc in enumerate(doc_list):
        for word in doc.split():
            if not search_index.get(word):
                search_index[word] = [0] * doc_cnt
            search_index[word][doc_num] += 1

    return search_index


def get_words(cnt_rows):
    return (input() for _ in range(cnt_rows))


def get_relevants(search_index, request):
    relevants = [[i, 0] for i in range(1, cnt_doc_rows + 1)]
    for word in set(request.split()):
        values = search_index.get(word)
        if not values:
            continue
        for doc_num, el in enumerate(values):
            relevants[doc_num][1] += el
    return relevants


if __name__ == '__main__':
    cnt_doc_rows = int(input())
    doc_list = get_words(cnt_doc_rows)
    search_index = get_search_index(doc_list, cnt_doc_rows)

    cnt_requests_rows = int(input())
    requests = get_words(cnt_requests_rows)
    for request in requests:
        relevants = get_relevants(search_index, request)
        relevants.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        for i, [doc_num, relevant] in enumerate(relevants):
            if i > 4 or relevant == 0:
                print()
                break
            print(doc_num, end=' ')
