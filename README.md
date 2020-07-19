# pymasssheilder

# Testing


## 1. Generate the Public and Private Keys

```python
import pymassshielder

bit_length = int(input("Enter bit length: "))

public_k, private_k = generate_keypair(2**bit_length)
```

## 2. Generate Cipher Text

```python
plain_txt = input("Enter a message: ")
cipher_txt, cipher_obj = encrypt(plain_txt, public_k)
print("Encrypted message: {}".format(cipher_txt))
```

## 3. Get back our plain text

```
print("Decrypted message: {}".format(decrypt(cipher_obj, private_k)))
```