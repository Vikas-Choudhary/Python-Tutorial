#String Capitalization
lower_cased = "this sentence needs to be capitalized."

cap_string = lower_cased[0].upper() + lower_cased[1:]
print(cap_string)



#Splitting the text:) itno list
text = "Some string, with some stuff."
print(text.split())
print(text.split(","))




#String Substiturion woth format
text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)

text = "This is another {variable_a} formatted string with \
multiple variables like {a} {b} {c}.".format(
    variable_a="variable based", 
    a="some random", b="replacement", c="text")
print(text)

text = """So, {name}, the best part is formated strings you don't have to order it. 
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously {name}, this is some fun formatting.""".format(
            name="Jerry", 
            var_a="Variable 1", 
            var_b="Variable 2")
print(text)

#Format with Arguments

text = "This is {0} formatted string".format("argument based")
print(text)

text = "This is another {0} formatted string \
with multiple variables like {1} {2} {3}.".format(
    "variable based", 
    "some random", 
    "replacement", 
    "text"
    )
print(text)

text = """So, {0}, the best part is formated strings you don't have to order it. 
And these argument replacements, ({1}, {2}, {0}) can be reused over and over.
Seriously {0}, this is some fun formatting.""".format(
            "Jerry", 
            "Variable 1", 
            "Variable 2")
print(text)


#%s Substitution

text = "This is %s formatted string" %("replacement")
print(text)

text = "The %%s format string is not as %s, but still very %s." %("robust", "useful")
print(text)




#%f Float Substitution

text = "0 decimal places: %.0f" %(20)
print(text)


text = "2 decimal places: %.2f" %(20)
print(text)

text = "10 decimal places: %.10f" %(20)
print(text)





#Date Substitution Docs
import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)


now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)