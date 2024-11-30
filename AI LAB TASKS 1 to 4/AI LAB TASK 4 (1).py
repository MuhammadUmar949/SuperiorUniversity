cardNumber=[4,7,8,2,7,8,0,0,0,1,6,1,6,4,0,1]
#cardNumber=[4,6,4,9,5,1,0,2,0,7,0,4,9,7,3,2]

#Step 1 Remove the last value

cardNumber.pop()
print(cardNumber)
# Step 2 Reverse the list
cardNumber.reverse()
print(cardNumber)

#step 3 double the even index
for i in range(0,len(cardNumber)):
    if i % 2==0:
        cardNumber[i]*=2
       
print(cardNumber)

# step 4    Sbtract by  that higher than 9
for i in range(0,len(cardNumber)):
    if cardNumber[i] >= 9:
        cardNumber[i]-=9


print(cardNumber)


#step 5 sum all the elements
sumOfList=sum(cardNumber)+1
print(sumOfList)
if sumOfList %10==0:
    print("Valid card")
else:
    print("Not Valid Card")    