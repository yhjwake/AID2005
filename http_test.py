"""
http 请求响应演示
"""

from socket import *
#创建套接字
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
c,addr=s.accept()
print("Connect from",addr)
data=c.recv(8888)
print(data.decode())

html="""HTTP/1.1 200 OK
Content-Yype:text/html

hello world
"""
c.send(html.encode())

c.close()
s.close()
