msg = "HELLO"
key = 42

encrypted = [ord(c)^key for c in msg]

decrypted = "".join(chr(c^key) for c in encrypted)

print("Original:", msg)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)