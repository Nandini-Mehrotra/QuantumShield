from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

msg = b"ORIGINAL AI MODEL"

signature = private_key.sign(msg)

print("Signature:", signature.hex())

try:
    public_key.verify(signature, msg)
    print("Signature valid")

except InvalidSignature:
    print("Signature invalid")

modified = b"MODIFIED AI MODEL"

try:
    public_key.verify(signature, modified)
    print("Modified model accepted")

except InvalidSignature:
    print("Tampering detected")