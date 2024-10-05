#create
food={}
def create():
    n=int(input("enter length of dictionary"))
    for i in range(n):
        key=input("enter key ")
        value=input("enter value ")
        food[key]=value
    return food
#add

def add(food):
    key=input("enter key for addition ")
    value=input("enter value ")
    food[key]=value
    return food

#delete
def delt(food):
    key=input("enter key to delete : ")
    del food[key]
    return food

#find value
def find(food):
    key=input("enter key to find ")
    print(food.get(key))
def printall(food):
    for i in food:
        data=food[i]
        print(i , ":" , data)
def frequency_count():
    data=input("enter data or sentence : ")
    freq={}
    for c in data:
        freq[c]=freq.get(c,0)+1
    for key in freq:
        print(key,freq[key])
while(1):
    print("choose one : \n\n")
    print("1.create")
    print("2.add ")
    print("3. delete")
    print("4. find ")
    print("5. print all")
    print("6.frequency count")
    choice=int(input("ente your  choice "))
    if choice==1:
        fooddata=create()
        print("dictionary created " ,fooddata)
    elif choice==2:
        fooddata=add(fooddata)
        print("dictionary after addition " , fooddata)
    elif choice==3:
        fooddata=delt(fooddata)
        print("dictionary after deletion " , fooddata)
    elif choice==4:
        find(fooddata)
    elif choice==5:
        printall(fooddata)
    elif choice==6:
        frequency_count()
        
    else:
        print("invalid choice ")
        break
