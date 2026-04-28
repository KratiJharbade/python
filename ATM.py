balance=int(input("Enter the balance:- "))
withdraw=int(input("Enter the amt u want to withdraw:- "))
if withdraw - (balance<1000):
    print("Transaction failed:Minimum balance violation")


