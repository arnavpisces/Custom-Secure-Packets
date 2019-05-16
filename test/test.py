import hashlib
class secureData:
    header='md5'
    data='this is the data'
    verify=''

a=secureData()
a.verify="dfasfd"
aa=a.encode()
bb=aa.decode()
c=(secureData)(bb)
print(c.verify)