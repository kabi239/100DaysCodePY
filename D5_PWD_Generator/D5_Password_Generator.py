#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to PY Password Generator")
L=int(input("how many letters would you like in your password?"))
S=int(input("how many symbols would you like in your password?"))
N=int(input("how many numbers would you like in your password?"))
 
pwd_list=[]
for i in range(0,L+1):
    pwd_list.append(random.choice(letters))
for i in range(0,S+1):
    pwd_list.append(random.choice(symbols))
for i in range(0,N+1):
    pwd_list.append(random.choice(numbers))

print(pwd_list)
random.shuffle(pwd_list)
password =""
for i in pwd_list:
    password+=i
print(f"Your Password is : {password}")