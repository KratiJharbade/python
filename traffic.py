speed=int(input("Enter The speed:- "))
repeated=int(input("If Repeated(yes/no):-"))
fine=0
if speed>100:
    if repeated=="yes":
        fine=1000*2
    else:
        fine=1000
    fine=1000
elif speed>80:
    if repeated=="yes":
        fine=500*2
    else:
        fine=500
    fine=500
print("The fine is:- ",fine)

