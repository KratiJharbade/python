'''
A
A B 
A B C
A B C D
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()