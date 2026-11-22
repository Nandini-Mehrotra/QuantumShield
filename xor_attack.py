encrypted = [98, 111, 102, 102, 101]

for key in range(256):
    decrypted = "".join(chr(c^key) for c in encrypted)

    if decrypted.isascii() and decrypted.isalpha():
        print("Key:", key, "Message:", decrypted)