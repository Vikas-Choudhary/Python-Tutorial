#Day_5
#playing with random stuff
items= ["Saurabh","Phone",123.22, 45 ,"School","Work","Classes",2000]
str_items=["Veronica","Sachin","Saurabh","Nitisha", "Deepika","Michael","Siddharth","John"]
int_items=[20,35,25,45,69,100,-1,30.2,12,11,22]
# same list,

# a-z 
str_items.sort(key=str.lower)
str_items

# z-a
str_items.sort(key=str.lower, reverse=True)
str_items.sort(key=str.upper, reverse=True)


# Smallest - Largest
int_items.sort()

# Largest - Smallest
int_items.sort(reverse = True)
print(int_items)

#To not modify the current list, use "sorted"
new_list = sorted(str_items, reverse=True)

def parse_lists(some_list):
	strl_items=[]
	numl_items=[]
	for i in some_list:
 		if isinstance(i,float) or isinstance(i,int):
 				numl_items.append(i)
 		elif isinstance(i,str):
 				strl_items.append(i)
 		else:
 			pass
	return strl_items,numl_items
 
print(parse_lists(items))

def calAvg(some_list):
	numl_items=[]
	count=0
	for i in some_list:
 		if isinstance(i,float) or isinstance(i,int):
 				numl_items.append(i)
 				count+=1
 		else:
 			pass

	total=sum(numl_items)
	avg=total/(count)*1.0
	return avg
print(calAvg(items))
