num=int(input("enter num:"))
for i in range(0,num):
    print(*range(i+1)) #1,12,123,1234
for i in range(15):
    print(*[i]*i)    #perfect row pyramids line ma jay 1,22,333,4444,55555  to aa use thay5
# for reverse use     
for i in range(15,0,-1):
    print(*[i]*i)   
for i in range(10,0,-1):
    print("*"*i)    
#for pyramid pattern
num=int(input("enter num:"))
for i in range(num):
    print(" "*(num-i)+"* "*(i))