import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

p = int(input("Enter the value for p :"))
q = int(input("Enter the value for q :"))
n = p*q
phi = (p-1)*(q-1)
e=d=2

while e>1 and e<phi:
    if gcd(e,phi) == 1:
        break
    e +=1
    
while d>1 and d<phi:
    if (d*e) % phi == 1:
        break
    d +=1
    
pt=input("Enter the text Message :")
print("\nn =",n,"\nphi =",phi,"\ne =",e,"\nd =",d)

ct=[(ord(char) ** e) % n for char in pt]
print("Cipher Text :")
for i in ct:print(i,end=" ")

et=[chr((char ** d) % n) for char in ct]
dt=''.join(et)

print("\nDecrypted text :",dt)