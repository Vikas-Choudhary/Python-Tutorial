import sys
#Taking away the spaces in Python :)
z=input("Enter the string1: ")

words=z.split()
for i in words:
	print(i)

#prints without putting new list items in the next line
t=input("Enter the string2: ")
wordss=t.split()
for i in range(0,len(words)) :
	sys.stdout.write(str(wordss[i]))

print("\n")

#prints without putting new list items in the next line and reverses it
y=input("Enter the string3: ")
list =[]
list=y.split()
list.reverse()
print (''.join([str(list[i]) for i in range (0,len(list))]))

