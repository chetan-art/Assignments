#1. Write a Python program to sum all the items in a list.
x = [3,4,1,3]
total=0
# output => 11
for i in range(0,len(x)):
	total=total+x[i]
print("the sum of list is :",total)

print("********************************************************")
#2. Write a Python program to multiplies all the items in a list
x = [3,4,1,3]
# output => 36
product= 1
sum=0
for i in x:
	product=product*i
	print(product)  
print("the multiplication of list is:",product)
print("********************************************************")
#3. Write a Python program to get the largest number from a list.
x = [3,4,1,3]
# output => 4
print("the largest number is", max(x))
print("********************************************************")
#3. Write a Python program to get the largest number from a list.
x = [3,4,1,3]
# output => 4
x.sort()
print("the largest number is", x)
print("********************************************************")
#4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
data = ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
temp=0
for i in data:
	if len(i) >=2 and i[0]==i[-1]:
		temp=temp+1
print(temp)
print("********************************************************")
#5. Write a Python program to remove duplicates from a list.
alist = [11,2,11,3,4,4,1,1,1]
d = {}
for i in range(0,len(alist)):
	d[alist[i]]=1
print(d.keys())
print("********************************************************")
#6. Write a Python program to print the numbers of from specified list after removing even numbers from it.
alist = [11,2,3,4,4,1,1,1]
# Expected out = [11,3,1,1,1]
for i in alist[:]:
	if i%2==0:
		print(i)
		alist.remove(i)
print(alist)
print("**********************************************************")
#7. Write a Python program to clone or copy a list.
# copy one list to another
list1=[4,5,6,7,9]
list2=list1
print(list1)
print(list2)
print("***********************************************************")
#9. Write a Python program to convert a list of elements into a string (should work for any 1 dimensional list)
a = ['a', 'c', 'c', 23, 1,'d']
# sample string = "acc231d"
string = ""
for i in a:
	string=string+str(i)
print(string)
print("************************************************************")
#10. Write a Python program to get the frequency of the elements in a list.
alist = [11,2,3,4,4,1,1,1]
# sample =>  { 11:1, 2:1, 3:1, 4:2, 1:3 }
dict1= {}
for i in alist:
	if i in dict1:
		dict1[i] +=1
	else:
		dict1[i]=1
print(dict1)
print("************************************************************")
#11. Write a Python program to insert an element before each element of a list.
alist = [4, 5, 6]
a = 10
list5=[]
string6=[]
# sample => [10, 4, 10,5,10,6]
for i in alist:
	string6=int(a)+int(i)
	list5.append(string6)
print(list(list5))
print("*************************************************************")
#12. Write a Python program to replace the last element in a list with another list.
data = [1, 3, 5, 7, 9, 10]
slist1=[2, 4, 6, 8]
#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
data.sort()
data.remove(10)
data=data+slist1
print(data)
print("**************************************************************")
#13. Write a Python program to insert a given string at the beginning of all items in a list.
list2 = [1,2,3,4]
string = "emp"
string2=""
list4 =[]
#Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
for i in list2:
	string2=string+(str(i))
	list4.append(string2)
print(list4)
print("**************************************************************")
#14. Write a Python program to count the number of characters (character frequency) in a string.
element1 = "google.com"
dict1={}
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
for i in element1:
	if i in dict1:
		dict1[i] +=1
	else:
		dict1[i]=1
print(dict1)
print("****************************************************************")
#17. Write a Python program to iterate over dictionaries using for loops.
data = {1:2,34:56, 67:9}
# Expected below output
#1 2
#34 56
#67 9
for key,value in data.items():
	print(key, value)
print("****************************************************************")
data = {1:2,34:56, 67:9}
# Expected below output
#1 2
#34 56
#67 9
for i in data:
	print(i,data[i])
print("*******************************************************************")
#18. Write a Python script to create a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#Dictionary= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d=dict()
for i in range(1,16):
	d[i]=i **2
print(d)
print("********************************************************************")
#19. Write a Python program to map two lists into a dictionary.
a = ['a', 'b', 'c']
b = [1,2,3]
# sample : {'a':1, 'b':2, 'c':3}
items=dict()
for i in a:
	for j in b:
		items[i]=j
		b.remove(j)
		break
print(items)
print("*********************************************************************")
#20. Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d=Counter(d1)+Counter(d2)
print(d)
print("************************************************************************")
#20. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
for i in d2:
	if i in d1:
		d2[i]=d2[i]+d1[i]
	else:
		pass
print(d2)
print("***********************************************************************")
#21. Write a Python program to print all unique values in a dictionary. Try after 3rd chapter
list7 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
new_list=[]
for i in (list7):
	for j in i:
		if i[j] not in new_list:
			new_list.append(i[j])
		else:
			pass
print(new_list)
print("****************************************************************************")

