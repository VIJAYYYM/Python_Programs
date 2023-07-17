a=int(input("A:"))
b=int(input("B:"))
operation=input("add/mul/div/sub:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="div"):
    print(a/b)
elif(operation=="mul"):
    print(a*b)
else:
    print("Invalid operation")
