data=str(input("enter data to be encrypted : "))
alphabet="abcdefghijklmnopqrstuvwxyz"
#key=5(no difference in output bcz u r adding 5 n subtracting 5 so no need).
encrypt=''
decrypt=''
for i in data:
    position=alphabet.find(i)
    newposition=(position+5)%26
    encrypt+=alphabet[newposition]
print("the encrypted text is",encrypt)
for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-5)%26
    decrypt+=alphabet[newpos]
print("the decrypted text is",decrypt)