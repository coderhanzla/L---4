num = int(input("Enter the Number: "))

if num > 1:
    for i in range(2 , int(num**0.5) ,+1):
         

         if num%i==0:
             print("It is Not a Prime Number")
             break

    else:
        print("  It is a prime Number")

