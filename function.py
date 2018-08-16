import hashlib


def hash_code(s, salt='nemo'):
    md5 = hashlib.md5()
    s += salt
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    print(hash_code('123'))

