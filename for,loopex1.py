#for loop with range
for i in range(11,21):
    print(i)
#for loop with list    
fruits=["apple","bpple","canana"]
for fruit in fruits:
    print(fruit)    
#iterate list numbers
lst_numbers = [11,23,34,4,5,7] 
sum=0
for i in lst_numbers:
    sum=sum+i
print(sum)       
lst_numbers = [11,23,34,4,5,7,2,"hello"]
sum=0
for i in lst_numbers:
    if isinstance(i,(int,float)):
        sum=sum+i
print(sum)        
