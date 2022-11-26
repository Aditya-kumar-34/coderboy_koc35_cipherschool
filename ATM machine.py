
print("welcome to canara bank")
p=int(input("Enter To your 4 digit pin number:"))
m=25000
if(p==1234):
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast cash")
    c=int(input("Please choose transaction:"))
    if(c==1):
        w=int(input("enter Withdraw amount:"))
        if(w<m and w%100==0):
            print("please take Your amount:",w)
        
    
            
        else:
            print("invalid cash")
    elif (c==2):
        print("Your available amount:",m)
    elif (c==3):
        print("1->5000")
        print("2->10000")
        print("3-150000")
        print("4-200000")
        f= int(input("Enter fast cash option:"))
        if(f==1 and 5000<m):
            print("please take cash 5000")
        elif(f==2 and 10000<m):
            print("please take cash 10000")
        elif(f==3 and 15000<m):
            print("please take cash 15000")
        elif(f==4 and 20000<m):
            print("please take cash 20000")
        else:
            print("invalid fast cash option")
else:
    print("Wrong choice") 












