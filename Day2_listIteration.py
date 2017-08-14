
#If you loop over a list, it's best to avoid changing the list in the loop body.
colours = ["red"]
for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)
#['red', 'black', 'white']



#To avoid these side effects, it's best to work on a copy by using the slicing operator, as can be seen in the next example:
colours = ["red"]
for i in colours[:]:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)
#['red', 'black']
#We still might have done something, what we shouldn't have done. We changed the list "colours", but our change hasn't had any effect on the loop anymore. 
#The elements to be looped remained the same during the iterations. 
