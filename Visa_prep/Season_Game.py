x=int(input())
if 1<=x<=12:
    if x in [3,4,5]:
        print("Spring")
    elif x in [6,7,8]:
        print("Summer")
    elif x in [9,10,11]:
        print("Autumn")
    elif x in [12,1,2]:
        print("Winter")
else:
    print("Invalid")
