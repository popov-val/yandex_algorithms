def get_cnt_words(cnt_words, input_str, num_doc):
    for word in input_str.split():
        if cnt_words.get(word):
            cnt_words[word] += 1
        else:
            cnt_words[word] = 1
    return cnt_words


if __name__ == '__main__':
    docs = {}
    cnt_docs = int(input())
    for i in range(1, cnt_docs + 1):
        docs[i] = get_cnt_words(input())

    print(1)
