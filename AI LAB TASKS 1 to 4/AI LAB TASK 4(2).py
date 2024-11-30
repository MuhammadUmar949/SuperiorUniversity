
def RemovePuntuations(string):
    string=list(string)
    templist=[]
    for char in string:
        tempvar=ord(char)
        if (tempvar>=65 and tempvar<=90) or(tempvar>=97 and tempvar<=122) or(tempvar>=48 and tempvar<=57):
            templist.append(char)

    string=''.join(templist)
    print(string)

string=input("Enter String: ")
RemovePuntuations(string)