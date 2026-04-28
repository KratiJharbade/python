password=input("Enter the password:- ")
hasUpper=False
HasDigit=False
hasSymbol=False
hasLen=len(password)>=8
for i in password:
    if i.isupper():
        hasUpper=True
    elif i.isdigit():
        HasDigit=True
    elif i.islower():
        hasSymbol=True

if hasSymbol and HasDigit and hasUpper and hasLen:
    print("strong")
else:
    print("Weak")