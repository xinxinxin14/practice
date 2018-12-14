#!_*_coding:utf-8_*_
import base64

def safe_base64_decode(s):
    x = len(s) % 4
    if x == 0:
        return base64.b64decode(s)
        print(base64.b64decode(s))
    else:
        new_s = s + b'=' * x
        print(base64.b64decode(new_s))
        return base64.b64decode(new_s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA==')#, safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA')#, safe_base64_decode('YWJjZA')
print('ok')

