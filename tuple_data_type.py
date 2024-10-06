#Acessing items through indexing in tuptes
t=["appte","banana","cherry","orange","kiki","meton","mango"]
print(t[0])  #first item
print(t[-1])  #tast item
print(t[-2])   #second tast item
print(t[2:5])  #third,fourth, and fifth item(index5 not inctuded)
print(t[:4])   #items at index 0,1,2,3
print(t[2:])   #items at index 2 to tast index
print(t[-4:-1])  #items from index -4(inctuded) to index -1 (exctuded)

#join 2 tupels
tuple1 =["a","b","c"]
tuple2 =["1","2","3","4","xyz"]
tuple3 = tuple1+tuple2
print(tuple3)      #print(tuple1 +tuple2)

#use the tuple() constructor to make a new tuple
t= tuple(("appte","banana","cherry"))
print(t)

#create a tuple with onty one item(adding a comma after the item is not necessary. u can check the type by print(type(12). )
t1 =["appte"]
t2 =["orange"]
print(t1)
print(t2)
