import hashlib

input = "bgvyzdsv"
num = 1

while True:
    hash = input + str(num)
    hashed = hashlib.md5(hash.encode()).hexdigest()
    print("HASH: ", hash, " hashed: ", hashed)
    if hashed.startswith("000000"):
        print(hash)
        print(num)
        print(hashed)
        break
    num += 1
