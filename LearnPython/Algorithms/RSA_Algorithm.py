# total time (1h30')
# Understand RSA Algorithm (20')
# Identify the main problem (10')
# Understand the problem (20')
# What Algorithms are used? (5')
# How to implement each Algorithm? (30')
# Find out what Question to ask for each Algorithm? (10')
# What knowledge is required for each Algorithm? (10')
# Implement the RSA Algorithm (15')
import math
import random

'''
Exercise:
    1) Cho n = 1234, a = 17855, b = 3456. Giá trị của biểu thức (a*b) mod n là bao nhiêu?
    asw: 710
'''

n = 1234
a = 17855
b = 3456
print(a*b % n) #710

def gcd(a, b):
  """Recursive implementation of the Euclidean Algorithm for GCD"""
  if b == 0:
    # co-prime
    return a
  else:
    return gcd(b, a % b)

'''
    2) Trong hệ mật mã RSA, Alice chọn 2 số nguyên tố p = 37, q = 43.
    Hỏi Alice phải chọn e bằng bao nhiêu là hợp lệ?
    asw: 1512
'''
p = 37
q = 43
n = p * q # 1591
phi_n = (p - 1) * (q - 1) # 1512

# e = 1 < e < phi_n
# algorithm to find e
# !% N and phi(n) are coprime
for i in range(2, phi_n): # stat from 2 because 1 is always coprime
  if (i % 2 != 0) and (gcd(i, phi_n) == 1):
    e = i
    print('Alice e:', e)
    break

'''
  3) Trong hệ mật mã RSA, Alice chọn 2 số nguyên tố p = 7, q = 11 và e = 7.
  Hỏi khoá bí mật d của Alice là bao nhiêu?
  ans: 43
'''
def multiplicative_inverse(e, phi):
  """Multiplicative Inverse"""
  d = 0
  while True:
    if (e * d) % phi == 1:
      return d
    d += 1

# p = 7
# q = 11
# n  = p * q # 77
# e = 7
# phi_n = (p - 1) * (q - 1) # 60
#
# d = multiplicative_inverse(e, phi_n)
# print(d)
'''
    4) Alice sử dụng hệ mật mã RSA, có cặp khóa bí mật là (d,n) = (5,95).
    Alice nhận được bản mã từ Bob là 132. Hỏi bản rõ Bob gửi là bao nhiêu?
    
    Bob's original message: 132 ^ 5 (mod 95) = 37
'''


def decrypt(private_key, ciphertext):
    """Decrypts ciphertext using the private key."""
    key, n = private_key
    plaintext = pow(ciphertext, key, n)
    return plaintext

# Alice's private key
private_key = (5, 95)

# Ciphertext received from Bob
ciphertext = 132

# Decrypt the message
plaintext = decrypt(private_key, ciphertext)

print("Bob's original message:", plaintext)
