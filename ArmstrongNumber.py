n = int(input("Enter The Number : "))

nod = len(str(n))
total =0
num =n 
while num>0:
    LD = num%10
    total += LD**nod
    num = num // 10   
if total==n:
    print("This is Armstrong Number..")
else:
    print("This is Not Armstrong Number..")