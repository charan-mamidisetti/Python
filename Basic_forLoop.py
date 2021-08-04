#Sum of a List using for loop
list= 1,4,5,6,6,3,56
sum=0
for i in list:
    sum= sum+i
print(sum)
---------------------------------------------

#program to iterate through the list with indexing
genre='pop','rock','zaz'
for i in range(len(genre)):
    print("i like",genre[i])
---------------------------------------------    
    
# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
for student in marks:
    if student==student_name:
        print(student[marks])
else:
    print("No student with that name")
---------------------------------------------   
    
# Get the number table
num= int(input("Enter the number:"))
for i in range(1,11):
    n=num*i
    print(num,"x",i,"=",n)
---------------------------------------------
