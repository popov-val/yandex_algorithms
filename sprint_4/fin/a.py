# https://contest.yandex.ru/contest/24414/run-report/132146921/
"""
-- ПРИНЦИП РАБОТЫ --
1) Читаем данные
2) Собираем поисковый индекс
    2.1) Пробегаемся по каждому документу
    2.2) Разделяем на каждое слово
    2.3) Собираем структуру вида:
        {
            <word> : {
                <номер документа>:<кол-во вхождений в документ>
            }
        }
3) Читаем запрос
4) Расчитываем релевантность
    4.1) Пробегаемся по каждому запросу
    4.2) Разделяем на каждое уникальное слово
    4.3) Собираем структуру вида:
        [[<номер документа>, <релевантность>]...]
5) Сортируем
    5.1) Сортировка происходит по релевантности по убыванию, номер документа по возрастанию
6) Выводим
    6.1) Проверяем на 0 и количество документов

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Поисковый индекс собираемся по каждому слову каждого документа
Релевантность рассчитывается на основе поискового индекса

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Кол-во документов - N
Кол-во слов в документе/запросе - L
Длина слова в документе/запросе - M
Кол-во слов в запросе - K, кол-во уникальных: лучший случай - 1, худший K
1) Сбор поискового индекса
    O(N) - Прохождение по каждому документу
        O(L*M) - Разбиение документа на слова (на каждый документ)
        O(L) - Прохождение по каждому слову (на каждый документ)
            O(M) - Расчет хэша для добавления к словарю (на каждый документ)
            O(1) - Добавление к словарю каждого слова (на каждый документ)
Итого: O(N*(L*M + L + L*M + L*1)) ~ O(N*L*M)
2) Поиск и расчет релевантности на каждый запрос
    O(N) - Формирование структуры релевантности
    O(L*M) - Разбиение запроса на слова
    O(K) - Формирование уникальных слов
    O(K*N) - Проход по каждому (уникальному) слову и добавление к структуре
        O(1) - Получение каждого слова по индексу для кождого слова
    O(NlogN) - сортировка структуры релевантности
Итого: O(N) + O(L*M) + O(K) + O(K*N) + O(NlogN) ~ O(K*N + L*M) на каждый запрос

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Кол-во документов - N
Кол-во слов в документе - L, кол-во уникальных: лучший случай - 1, худший L
Кол-во слов в запросе - K, кол-во уникальных: лучший случай - 1, худший K
Длина слова в документе/запросе - M
1) Сбор поискового индекса - O(L*N*M) для каждого уникального слова словарь с кол-вом документов
2) Поиск и расчет релевантности на каждый запрос O(N) + O(K) + O(M) на структуру релевантности
    и уникальные слова в запросе
"""

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
