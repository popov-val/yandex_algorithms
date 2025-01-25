# https://contest.yandex.ru/contest/24414/run-report/132200277/
"""
-- ПРИНЦИП РАБОТЫ --
1) Читаем данные
2) Создаем экземпляр хэш-таблицы, расчет корзин происходит через значение близкое к золотому сечению
3) Читаем команды и параметры
4) Выполняем и выводим

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Расчет индекса корзины происходит через формулу (h*s*mod2**32)>>(32−p)
В случае колизии добавляем в конце списка

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В худщем случае O(N) - если все значения попали в одну корзину
В лучшем случае O(1) - если все значения попали в разные корзины

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(N) - на хэш-таблицу

"""
import math


class HashTable:
    def __init__(self, p):
        self._s = 2654435769
        self._d = 2 ** 32
        self._p = p
        self._m = 2 ** p
        self._table = [[] for _ in range(self._m)]

    def __str__(self):
        return f'{self._table}'

    def _get_bucket(self, key):
        num = (key * self._s) % self._d
        diff = 32 - self._p
        return self._table[num >> diff]

    def _get_index_in_bucket(self, bucket, key):
        for (i, (k, v)) in enumerate(bucket):
            if k == key:
                return i

    def put(self, key, value):
        bucket = self._get_bucket(key)
        index = self._get_index_in_bucket(bucket, key)
        if index is None:
            bucket.append((key, value))
        else:
            bucket[index] = key, value

    def get(self, key):
        bucket = self._get_bucket(key)
        index = self._get_index_in_bucket(bucket, key)
        if index is not None:
            return bucket[index][1]

    def delete(self, key):
        bucket = self._get_bucket(key)
        index = self._get_index_in_bucket(bucket, key)
        if index is not None:
            k, v = bucket.pop(index)
            return v


if __name__ == '__main__':
    n = int(input())
    # Ниже считаем кол-во корзин, так как должна быть степень двойки
    # Предполагаем что количество значений около половины команд
    hash_tab = HashTable(int(math.log(n / 2, 2)))
    for _ in range(n):
        command_name, *args_str = input().split()
        args = [int(arg) for arg in args_str]
        command = getattr(hash_tab, command_name)
        output = command(*args)
        if command_name != 'put':
            print(output)
