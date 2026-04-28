unit=float(input("Enter the units:- "))
i=50

if unit<=100:
    i+=unit*1.5
elif unit<=200:
    i+=100*1.5+(unit-100)*3.5
else:
    i+=100*1.5+100*3.5+(unit-200)*5
if i>2000:
    i=i*1.1

print("Total Bill= ",i)