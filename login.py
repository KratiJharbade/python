flag=0
for i in range(4):
    password=int("Enter the login attempts= ")
    if password =="42421":
        print("Login Successful")
        flag=1
        break
    else:
        print("Wrong Attempt")
if not flag:
    print("Account Logged!!!")