# socket是Python内置标准库，无需安装。
import socket as f
import json
from urllib.request import urlopen

# 全局取消证书验证
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 使用socket，先获取电脑的主机名后，再获取本机的IP地址。
hostn = f.gethostname()
Laptop = f.gethostbyname(hostn)

# 局域网IP
print(f"你的电脑本地IP地址是:{Laptop}")

# 获取电脑的公网IP地址，可以借助一些第三方网站
with urlopen(r"https://jsonip.com") as fp:
    content = fp.read().decode()
ip = json.loads(content)["ip"]
print(f"你的电脑公网IP地址是:{ip}")
