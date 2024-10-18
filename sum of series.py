l=input()
e=input()
s=input()
smy=l
n=1
while smy<=s :
    smy=smy+1/(n**2)
    n+=1
print(round(smy, e))