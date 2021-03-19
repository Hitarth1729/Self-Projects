num = int(input("Enter a number:"))
for i in range(2,int(num/2)+1):
    if num%i==0:
        print("The number is divisible by ",i)
        break

else:
    print("Prime")
