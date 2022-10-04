#percentage of varun and raghav
def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/4)
num1 = int(input("varun , enter your english marks  = "))    
num2 = int(input("varun , enter your marathi marks  = "))    
num3 = int(input("varun , enter your science marks  = "))    
num4 = int(input("varun , enter your mathamatics marks  = "))    
marks1  = [num1,num2,num3,num4]
varun_percentage = percent(marks1)
num5 = int(input("raghav ,enter your english marks  = "))    
num6 = int(input("raghav ,enter your marathi marks  = "))    
num7 = int(input("raghav ,enter your science marks  = "))    
num8 = int(input("raghav ,enter your mathamatics marks  = "))  
marks2 = [num5,num6,num7,num8]
raghav_percentage = percent(marks2)
print(f"varun u have {varun_percentage} percentage and raghav u have {raghav_percentage} percentage in final exam .")
