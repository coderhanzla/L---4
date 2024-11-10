
# s = int(input("Enter The Number Of Rows:"))

# for i in range( 1 , s+1 ):
#     for j in range(i):
#         print("*" , end = "")

#     print()


s = int(input("Enter The Number Of Rows:"))

for i in range(s ,0 , -1 ):
    for j in range(i , 0 , -1):
        print("*" , end = "")

    print()

