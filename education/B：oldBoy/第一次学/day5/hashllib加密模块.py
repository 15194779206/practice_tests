import hashlib

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.digest())
m.update(b"It's been a long time since last time we ...")

# print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash