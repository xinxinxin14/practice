import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python haslib?'.encode('utf-8'))

print(md5.hexdigest())


def calc_md5(password):
    password_md5 = hashlib.md5()
    password_md5.update(password.encode('utf-8'))
    return password_md5.hexdigest()

print(calc_md5('a3s2d1a3s2d'))


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user,password):
    if db[user] == calc_md5(password):
        return True
    else:
        False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')






















