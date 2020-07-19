<h1 align="center"><b>PyConfidentiality</b></h1>

![RSA](https://img.shields.io/badge/rsa-encrypted-brightgreen)
![Open Source](https://img.shields.io/badge/open-source-red)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/smaranjitghose/pycondidentiality/blob/master/LICENSE)
![Forks](https://img.shields.io/github/forks/smaranjitghose/pycondidentiality)
![Stars](https://img.shields.io/github/stars/smaranjitghose/pycondidentiality)

Adding secrecy to your emails with RSA!

<p align="center"><img width=50% src="https://media.giphy.com/media/3oKIPqZPlKW5otXIS4/giphy.gif"></p>

<h3 align="center"><b>Installation</b></h3>

```python
pip install pyconfidentiality
```

<h3 align="center"><b>Usage</b></h3>

## 1. Generate the Public and Private Keys

```python
from pyconfidentiality import generate_keypair

bit_length = int(input("Enter bit length: "))

public_key, private_key = generate_keypair(2**bit_length)
```

## 2. Generate Cipher Text

```python
from pyconfidentiality import encrypt_message
plain_text = input("Enter a message: ")
cipher_text, cipher_obj = encrypt_message(plain_text, public_key)
print("Encrypted message: {}".format(cipher_text))
```

## 3. Send the message

- Note we are intially using GMAIL for this
- Make sure your Google Account has [Allow Less Secure App Access](https://myaccount.google.com/lesssecureapps) enabled
- It is always recommeded to store the credentials of your GMAIL account using environment variables in your system

```python
from pyconfidentiality import send_message
your_email = os.environ.get('EMAIL_ID') 
your_password = os.environ.get('EMAIL_PASSWORD') 
receiver_email = input("Enter Reciever Email") 
subject = input("Enter subject of the Email") 

send_message(your_email,your_password,reciever_email,subject,cipher_text)
```

## 4. Get back our plain text

```python
from pyconfidentiality import decrypt_message
print("Decrypted message: {}".format(decrypt(cipher_obj, private_key)))
```

<h2 align= "center"><b> Project Maintainers</b></h2>

<p align="center">
<img width=20% src="https://avatars2.githubusercontent.com/u/46641503?v=4">&ensp;&ensp;&ensp;
<img width=20% src="https://avatars2.githubusercontent.com/u/40017559?v=4">
</p>

<a href="https://github.com/smaranjitghose">
<h4 align="center"><b>Smaranjit Ghose</b></a>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
<a href="https://github.com/anushbhatia"><b>Anush Bhatia</b></h4></a>


<a href="./Code_of_conduct.md"><h2 align= "center"><b> Code of Conduct</b></h2></a> 
<p align="center"><img width=35% src="https://media.giphy.com/media/qHRwTyhWIj4UU/200w_d.gif"></p>

<a href="./License.md"><h2 align= "center"><b> License</b></h2></a> 
<p align="center"><img width=35% src="https://media.giphy.com/media/xUPGcJGy8I928yIlAQ/giphy.gif"></p>

