# Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
# функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def count_hash(s) -> int:
    set_ = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(set_) - 1


str_ = "About a thousand years ago, people known as the Vikings were known and feared throughout Europe. " \
       "The Vikings were the people of the northern part of Europe, called Scandinavia, which includes the " \
       "modern countries of Denmark, Norway, and Sweden. The Vikings made their living by farming and fishing. " \
       "However, by about the year 700, they began making attacks, or raids, upon towns along the coasts of Europe " \
       "in order to steal the wealth of those towns."

print(f'В исходной троке есть {count_hash(str_)} различных подстрок')
