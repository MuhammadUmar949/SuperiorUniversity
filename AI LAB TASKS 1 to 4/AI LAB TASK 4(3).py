def SortText(word):
    word=word.lower()
    word=list(word)
    tempList1=[]
    for char in word:
        tempVar=ord(char)
        tempList1.append(tempVar)
    for i in range(0,len(tempList1)):
        for j in range(0,len(tempList1)):
            if tempList1[i]< tempList1[j]:
                tempList1[i],tempList1[j]=tempList1[j],tempList1[i]   
    
    tempList2=[]
    for char in tempList1:
        tempVar=chr(char)
        tempList2.append(tempVar)    
    word=''.join(tempList2)   
    print(word) 



word=input("Enter Test to sort: ")
SortText(word)