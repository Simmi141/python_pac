#We can assign a string to a variable:
a="Hello"
print(a)
print(a[0])

#we can assign a multiline string to a variable by using three single quotes:
b='''Hi everyone.
My self siddhi'''
print(b)

#we can assign a multiline string to a variable by using three double quotes:
c="""Hi everyone,
Myself siddhi"""
print (c)

#To conatenate, or combine, two strings we can use the + operator:
x="Hello"
y="Everyone"
z=x+" "+y
print(z)

#we cannot combine strings and numbers like this(No Output):
age=30
txt="My name is XYZ. I am "+age
print(txt)
