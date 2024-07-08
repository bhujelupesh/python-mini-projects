n = int(input("Enter the total number of subjects: "))

marks = []
print("The full marks of the subject must be 100")
for i in range (n):
    marks.append(float(input(f"Enter the marks of subject {i+1}: ")))

sumofmarks = sum(marks)
percentage = (sumofmarks / (n*100)) * 100

print(f"The total obtain marks is :{sumofmarks} and Percentage is : {percentage}")


if percentage >= 90 :
    print("Final grade : A")
    
elif percentage < 90 and percentage > 80 :
    print("Final grade : B")
    
elif percentage < 80 and percentage > 70 :
    print("Final grade : C")
    
elif percentage < 70 and percentage > 60 :
    print("Final grade : D")
    
else:
    print("Failed") 
    