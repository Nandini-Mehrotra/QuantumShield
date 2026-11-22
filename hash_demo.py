import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

original = "AI Model Version 1"
modified = "AI Model Version 2"

h1 = hash_data(original)
h2 = hash_data(modified)

print("Original hash:", h1)
print("Modified hash:", h2)

if h1 == h2:
    print("Integrity verified")
else:
    print("Tampering detected")