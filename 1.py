import hashlib


def substr_count(string: str):
    length = {}
    for i in range(len(string)):
        for j in range(len(string)):
            if j + i <= len(string) and string[j:j + i] != '':
                length.setdefault(hashlib.sha1(string[j:j + i].encode('utf-8')).hexdigest())
    # print(length)
    return len(length)


print(substr_count('hello'))
