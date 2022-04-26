import json
from hashlib import md5

s1 = '{"action":"xxx","params":{"a":1,"b":2},"secret":"balala"}'  # 前端json字符串，无空格
s2 = json.loads(s1)  # 解析前端json，转dict
s3 = json.dumps(s2, separators=(',', ':'))  # dict转json，不带空格
s4 = json.dumps(s2)  # dict转json，带空格
s5 = str(s2)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
# md5加密
print(md5(s1.encode('utf8')).hexdigest())
print(md5(s3.encode('utf8')).hexdigest())
print(md5(s4.encode('utf8')).hexdigest())
print(md5(s5.encode('utf8')).hexdigest())
