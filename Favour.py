
name= "Favour"
age= 15
height=1.85
print('Name:',name,'Age:',age,'Height:',height)

#basic arithmetic
x=10
y=5
print('Sum:',x+y)
print('Difference:',x-y)
print('Product:',x*y)
print('Division:',x/y)
print('Raise to the power:',x**y)

#conditional statement
num=6
if num%2==0:
    print("Even")
else:
    print("Odd")

#loops
print('For loops')
for i in range(1,6): 
  print(i)
  
print("While loop")
i=1
while i<=5:
    print(i)
    i+=1
    
#function
def square(num):
    return num*num
print(square(7))

#list
fruits=['orange','apple','lemon']
fruits.append('pineapple')
fruits.remove('orange')
print(fruits)

#dictionaries
person={
    "name":"musa",
     "age": 15,
     "city": "abuja"    
     }
print(person["age"])

    
