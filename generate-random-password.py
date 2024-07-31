import string
import random
len=int(input("Enter the length of passsword:"))

uppercase=string.ascii_uppercase
lowercase=string.ascii_lowercase
digits=string.digits
symbol=string.punctuation
str=uppercase+lowercase+digits+symbol
str = uppercase+lowercase+digits+symbol
pwd=random.sample(str,len)
password = "".join(pwd)
print(password)
