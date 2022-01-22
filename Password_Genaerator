import random
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['@', '#', '$', '%','_']
all=upcase+lowcase
dig=random.choice(nums)
lowalp=random.choice(lowcase)
upalp=random.choice(upcase)
sysm=random.choice(symbols)
al=random.choice(all)
temp_pass=lowalp+upalp+al+sysm+dig
list1=[]
for i in range(7):
    k=random.choice(all)
    list1.append(k)
list1.append(temp_pass)
passw=""
for x in list1:
    passw+=x
print(passw)
