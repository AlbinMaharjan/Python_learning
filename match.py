x=int(input("Enter a number :"))
# y=int(input("Enter a number :"))
match x:
    case 0:
        print("You cannot drive")
    
    case _ if x<=18:
        print("you cannot drive")
           
    case _ if x>18:
        print("you can drive")       
        
    case _:
         print(x)
            
            
    