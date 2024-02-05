a=int(input("enter a number: "))
n1 , n2 = 0 , 1 
sum = 0 
if a <= 0 :
    print("enter a valid number")
else:
    for i in range (0 , a):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
       