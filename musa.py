name= "musa"
age= 15
height=1.85
print(name,age,height)

#basic arithmetic
x=10
y=5
sum=x+y
difference= x-y
product=x*y
a=product/y
b=product**y
print(sum)
print(difference)
print(product)
print(a)
print(b)

#conditional statement
num=6
if num%2==0:
    print("even")
else:
    print("odd")

#loops
for i in range(1,6): 
  print(i)
  
print("while loop")
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

    
