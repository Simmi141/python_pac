#Acessing items through in lists
l=["apple","banana","cherry","orange","kiki","melon","mango"]
print(l[0])  #first item
print(l[-1])  #last item
print(l[-2])   #second last item
print(l[2:5])  #third,fourth, and fifth item(index5 not included)
print(l[:4])   #items at index 0,1,2,3
print(l[2:])   #items at index 2 to last index
print(l[-4:-1])  #items from index -4(included) to index -1 (excluded)

#join 2 lists
list1 =["a","b","c"]
list2 =["1","2","3","4","xyz"]
list3 = list1+list2
print(list3)      #print(list1 +list2)

#use the list() constructor to make a new list
l= list(("apple","banana","cherry"))
print(l)

#create a list with only one item(adding a comma after the item is not necessary. u can check the type by print(type(12). )
l1 =["apple"]
l2 =["orange"]
print(l1)
print(l2)
