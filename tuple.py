#ordered
t=("apple","banana","cherry")
print(t)

#unchangeable
#you can convert tuple into list, change the list & convert it back into tuple
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#allows duplicate members
td=("apple","apple","banana","cherry")
print(td)

#unchangeable(no output)
z=("apple","banana","cherry")
z[1]="kiwi"
print(z)
