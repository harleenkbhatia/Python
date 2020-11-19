'''
a= int(input("Enter the value from 1 to 12: ")) #1-12
month= "JanFebMarAprMayJunJulAugSepOctNovDec"
print(month[3:6])
print(month[3*(a-1):(3*(a-1))+3])
#indexing is from 0 therefore a-1 is used
'''
a= int(input("Enter the value from 1 to 7: "))
week= "MondaTuesdWedneThursFridaSaturSunda"
print(week[5:10])
print(week[5*(a-1) : (5*(a-1))+5])

