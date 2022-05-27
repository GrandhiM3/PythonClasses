'''
name='Murali'
age=31
salary = 250000.30
'''

name,age,salary = 'Murali',31,250000.30
#Approach 1
print(name)
print(age)
print(salary)
print(name,salary)
print(name,age)
print(age,salary)
print(name,age,salary)

#Approach 2
print("Name is:",name)
print("Age is:",age)
print("Salary is:",salary)

#Approach 3
print("Name is:%s Age is:%d Salary is:%g"%(name,age,salary))


#Approach 4 {}

print(print("Name is:{} Age is:{} Salary is:{}".format(name,age,salary)))

