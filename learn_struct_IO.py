import base64,struct


bmp_data = base64.b64decode(r'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
print(struct.unpack('<ccIIIIIIHH',bmp_data[:30]))

try:
    picture_draw = open(r'C:\Users\Administrator\Desktop\YWX\practice\random_draw.bmp','rb')
    print(picture_draw.read()[:30])

finally:
    if picture_draw:
        picture_draw.close()
        

def bmp_info(data):
    byte_unpack = struct.unpack('<ccIIIIIIHH',bmp_data[:30])
    if byte_unpack[0]== b'B'and byte_unpack[1] == b'M':
        print('the filetype of %s is bmp' % data)
        return {
            'width':byte_unpack[6],
            'height':byte_unpack[7],
            'color':byte_unpack[9]
            }
    else:
        print('the filetype of %s is not bmp' % data)



# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')


sbd = bmp_info(picture_draw)
print(sbd['width'])
print(sbd['height'])
print(sbd['color'])
