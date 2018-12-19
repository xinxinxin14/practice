from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
import time
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = '1090486553@qq.com'
password = 'dxfijwjwcouphiaf'

to_addr = 'yangwenxin_sti@126.com'

smtp_server = 'smtp.qq.com'


'''msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')
msg['From'] = _format_addr('Python爱好者<%s>'% from_addr)
msg['To'] = _format_addr('管理员<%s>'%to_addr)
msg['Subject'] = Header('greeting from smtp......','utf-8').encode()'''
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>'% from_addr)
msg['To'] = _format_addr('管理员<%s>'%to_addr)
msg['Subject'] = Header('greeting from smtp......','utf-8').encode()
msg.attach(MIMEText('send with file','plain','utf-8'))

with open(r'C:\Users\Administrator\Desktop\维修机双层\2537.png','rb') as f:
    mime = MIMEBase('image','png',filename='2537.png')
    mime.add_header('Content-Dispostion','attachment',filename='2537.png')
    mime.add_header('Content-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server,quit()
