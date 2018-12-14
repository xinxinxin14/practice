#!_*_ coding:utf-8_*_
import re
def is_valid_email(addr):
    wheth =  re.match(r'[0-9a-zA-Z\.\_]*@[0-9A-Za-z]*.com',addr)
    print(wheth)
    if wheth:
        return True

    else:
        return False
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    if '<'and'>' in addr:
        name = re.match(r'<(.*)?>',addr)
        print(name)
        print(name.group(1))
        return name.group(1)
    else:
        name = re.match(r'(.*)?@',addr)
        print(name)
        print(name.group(1))
        return name.group(1)




# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
