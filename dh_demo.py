p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

secret_alice = pow(B, a, p)
secret_bob = pow(A, b, p)

print("Alice public value:", A)
print("Bob public value:", B)

print("Alice shared secret:", secret_alice)
print("Bob shared secret:", secret_bob)