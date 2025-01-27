# def average(a=20,b=10):
#     print("The average is",(a+b)/2)
    
# # average(10,5)    
# average()

def average(*number):
    sum=0
    for i in number:
        sum=sum+i
        avg=sum/len(number)
        return avg
c=average(10,5,9,7,8,9) 
print(c)  
#     print("Average is :",avg)    
        
        
# average(10,5,6,7,9,3,1,1)