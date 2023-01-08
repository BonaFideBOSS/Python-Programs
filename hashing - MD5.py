import hashlib
string = input("write something: ")
result = hashlib.md5(string.encode())
print(result.hexdigest())
