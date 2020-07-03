#2. How to find the type of a variable?
i = 10.4 # float
x = 100 # int
y = [1,2,3] # list
#Find & print the type of these variables
print(type(i))
print(type(y))
print(type(x))
print ("**********************************************************************")
#3. Swap string variable values
fname = "rahul"
lname = "dravid"
#Swap the value of variable with fname & fname with lname
#Output:: print(fname) # dravid
#		 print(lname) # rahul
out = lname
lname = fname
fname=out
print(fname) 
print(lname)
print ("**********************************************************************")
#4. Write a program to swap first & last element of any list provided
inp = [10,2,3,44,4]
#output: print(inp) # [4,2,3,44,10]
out=inp[0]
inp[0]=inp[4]
inp[4]=out
print(inp)
print ("**********************************************************************")
#5. Find length of below list
inp = [10,2,3,4]
print(len(inp))
print ("**********************************************************************")
#6. Find length & type of 2nd element in a list
inp1 = [10,2,30012,4] # expecting len - 5
inp2 = ["Rahul", "Ajay", 'xyz', 4]
print(type(inp1[2]))
print(type(inp2[2]))
print(len(inp1))
print(len(inp2))
print ("**********************************************************************")
#7. Remove last 2 elements from the list
inp = [10,2,3,4]
inp.remove(3)
inp.remove(4)
print(inp)
print ("**********************************************************************")
#9. Take below as input dictionary
sample = {
	"user1" : 'yogi',
	"user2" : 'booboo',
	"user3" : 'rupert',
	"user4" : 'teddy',
	"user5" : 'care',
	"user6" : 'winnie',
	"user7" : 'sooty',
	"user8" : 'padders',
	"user9"  : "polar",
	"user10" : 'grizzly',
	"user11" : 'baloo',
	"user12" : 'bungle',
	"user13" : 'fozzie',
	"user14" : 'huggy',
	"user15" : 'barnaby',
	"user16" : 'hair',
	"user17" : 'greppy'
}
#Perform basic operations like::
#	(a) user15 no longer has a machine assigned
#	(b) The name of user16's machine is changed to 'Ursa'
#	(c) user17 is leaving the company, and a new user, user18, will be assigned his machine
#	(d) user5, user6, and user7 are all leaving at exactly the same time, but their machine names are to be stored in a list called machines.
#	(e) Print a list of each (hint) user, with their machine, in any order. Do not print users that have no machine defined for them (like user15, for example) -> Try this after 2nd chapter.
sample.pop("user15")
sample["user16"]="ursa"
sample.pop("user17")
sample["user18"]="greppy"
print(sample)
print("******************************************************************************")
#10. Perform below operations on string
		# search and replace
inp = "c/home/test/abc.py"
		#update this to : c:\home\test\abc.py
print ("c\\home\\test\\abc.py")
inp = "google.com"
		#remove '.com' from above string
		#output : print(inp) # google
y=inp.replace(".com"," ")
		#find the position of '.' in above string
inp = "google.com"
x=inp.index(".")
print(y)
print(x)
print("******************************************************************************")
#11. Creating below mapping data in dictionary
inp= {
   "name" : "ajay",
   "rn"   : "10",
   "pan"  : "chxp34545s1"
}	
	#Get a keyboard input & display data which is mapped to input
	#ex: if keyboard input is name then display ajay
print(inp["name"])
print("******************************************************************************")
#12. Try a string operation to perform below operation
exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014
y=list(exam_st_date)
print(y)
z=str(exam_st_date)
print(z.replace(",","/"))
print("******************************************************************************")
#13. Write a statement to find the length of a number?
x = 1234342
y=str(x)
# print the length
print(type(y))
print(len(y))
z=int(y)
print(type(z))
#16. Write a program to remove last object from a tuple
x = (11,22,33,44)
# Expected => x = (11,22,33)
print(x[0:3])
print("******************************************************************************")
#18. Write a program to convert values of a dictionary to tuple
data = {11:22,33:44,55:66}
# Expected out = (22,44,66)
x=data.keys()
z=data.values()
print(x)
print(z)
print("******************************************************************************")
#21. Write a program to insert a key 10 value 20 into below dictionary
x = {11:22,33:44}
# Expected output: x = {11:22,33:44,10:20}
x.setdefault(10)
x[10]=20
print(x)
print("******************************************************************************")
#22. Write a program to convert string characters to list
x = "100ab"
# Expected output: x = ['1', '0', '0', 'a', 'b']
print(list(x))
print(x)
print("******************************************************************************")
#23. Reverse a string using slicing
inp = "1234"
# expected => out = "4321"
print(inp[-1::-1])
print("******************************************************************************")
#24. Write a program to get last 2 characters from a sring
inp = "ajay"
# expected output => out = "ay"
print(inp[-2::])
print("******************************************************************************")
#26. Given a string, fetch all odd position characters
#      0123456789
inp = "ajay kumar"
# expected output => out = "jykmr"
print(inp[1::2])
print("******************************************************************************")
#27. What is the expected output in below program?
#      0123456789
inp = "ajay kumar"
print(inp[1:-1]) #jay kuma
print(inp[9:-1]) # there is no character between the given range of index.
print("******************************************************************************")
#17. Find symmetric difference of 2 sets without using symmetric_difference method
x = {1,2,3,4}
y = {4,5,6,7}
# Expected out = {1,2,3,5,6,7} 
# (x-y)+(y-x)
#x.difference(y).union(y.difference(x))
x.update(y)
print(x)
z=print(x-y)
w=print(y-x)
#print(z+w)