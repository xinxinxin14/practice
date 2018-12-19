#_*_ coding:utf-8_*_
import itertools

'''natuals = itertools.count(1)
for n in natuals:
    print(n)
'''

'''cs = itertools.cycle('ABC')
s = 0
for c in cs:
    print(c)
'''



ns = itertools.repeat('haha',12)
for i in ns:
    print(i)


natuals = itertools.count(5)
ns = itertools.takewhile(lambda x:x<10,natuals)
print(list(ns))

for c in itertools.chain('ABC','XYZ'):
    print(c)

for key,group in itertools.groupby('AAAAAAAaaaaASSSSDsssDDdddDFFffffF',lambda c:c.upper()):
    print(key,list(group))
    

def pi(N):
    odd_sequence = itertools.count(1,2)
    previous_n = itertools.takewhile(lambda x:x<=2*N-1,odd_sequence)
    pi_sum = 0
    for i in previous_n:
        pi_sum +=  (-1)**((i+1)/2 + 1)*4/i
        print(pi_sum)
    return pi_sum




# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
