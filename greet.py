import time
times=time.strftime('%H:%M:%S')
print(times)
htime=int(time.strftime('%H'))
if(htime>=1 and htime<12):
    print("Good Morning Albin")
 
elif(htime>=12 and htime<5):
    print("Good Afternoon Albin") 
       
elif(htime>=5 and htime<7):
    print("Good Evening Albin")
    
else:
    print("Good Night Albin")    

