import hmac
import hashlib
import os

key = os.urandom(32)

msg = b"AI MODEL VERSION 1"

tag = hmac.new(key, msg, hashlib.sha256).hexdigest()

received = b"AI MODEL VERSION 2"

new_tag = hmac.new(
    key, received, hashlib.sha256
).hexdigest()

print("Original tag:", tag)
print("Received tag:", new_tag)

if hmac.compare_digest(tag, new_tag):
    print("Message verified")
else:
    print("Tampering detected")