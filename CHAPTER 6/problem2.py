#marks problem


a=int(input("Enter marks for English:"))
b=int(input("Enter marks for Science:"))
c=int(input("Enter marks for Maths:"))
# n=int(input("Enter the maximum marks: "))
total_percentage= 100*(a+b+c)/300

if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print (f"Passed,{total_percentage}%")
else:
    print (f"Failed,{total_percentage}%")

# if((a/n)*100>=per and (b/n)*100>=per and (c/n)*100>=per and (tot/(n*3))*100>=temp):
#     print("Passed")
# else:
#     print("Failed")                


