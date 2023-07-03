import hashlib
def program():
    string = input("write something: ")
    result = hashlib.md5(string.encode())
    print(result.hexdigest())
    program()
program()
