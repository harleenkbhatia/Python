sentence="My phone number is 9582673200 which starts with 98"
import re
pattern="[0-9]+" #single value
print(re.search(pattern,sentence))
print(re.findall(pattern,sentence))
print(len(re.findall(pattern,sentence)))
pattern="[0-9]*" #single value
print(re.search(pattern,sentence))
print(re.findall(pattern,sentence))
print(len(re.findall(pattern,sentence)))
sent="My phone number is harleen123"
pattern="[a-z0-9]*" #only small letter
print(re.findall(pattern,sent))
pattern="\w"
print(re.findall(pattern,sent))
pattern="[a-z]+[0-9]+"
print(re.findall(pattern,sent))
sent1="My name is Harleen and my email id is harleen123@gmail.com .\
      My friend's name is rahul and his email id is rahul1234_!'`~yo@yahoo.com"
pattern="\w+@[a-z]+.[a-z]+"#spcl char ni honge isse
print(re.findall(pattern,sent1))
pattern="[_!'`~a-zA-Z0-9]+@\w+.\w+"#check fromthe rec kya h
print(re.findall(pattern,sent1))
print(re.split("\s",sent1,4))
print(re.sub(pattern,"Email_id",sent1,1))