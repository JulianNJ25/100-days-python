import string
import random

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password")
passwd_len = int(input())

print("How many simbols would you like")
symbol_num = int(input())


print("How many numbers would you like?")
num_num = int(input())


passwd = []
for i in range(passwd_len):
    passwd.append(random.choice(string.ascii_letters))

for i in range(symbol_num):
    passwd.append(random.choice(string.punctuation))

for i in range(num_num):
    passwd.append(random.choice(string.digits))

random.shuffle(passwd)

final_passwd = ""
for char in passwd:
    final_passwd += char

print(f"\nYour generated password is: {final_passwd}")