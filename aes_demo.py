import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)

aes = AESGCM(key)

nonce = os.urandom(12)

msg = b"CONFIDENTIAL AI MODEL"

encrypted = aes.encrypt(nonce, msg, None)

decrypted = aes.decrypt(nonce, encrypted, None)

print("Original:", msg.decode())
print("Key:", key.hex())
print("Nonce:", nonce.hex())
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted.decode())

# for tamering

from cryptography.exceptions import InvalidTag

modified = bytearray(encrypted)
modified[0] ^= 1

try:
    aes.decrypt(nonce, bytes(modified), None)
    print("Accepted")

except InvalidTag:
    print("Tampering detected!")