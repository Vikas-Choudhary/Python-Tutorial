import datetime
def_names=['Saurabh','Veronica','raj','prem','Tessa','tia','RaDHE']
def_amts=[500.3,1230.996,250.53,450.530,1000,25.3,2503.63]
message="""Hi {name}! 
Thanks for the purchase on {date}. 
Just a reminder the purchase total was Rs {amount}
We hope to see you soon :)"""

def print_message(names,amounts):
	messages=[]
	if len(names)==len(amounts):
		i=0;
		today = datetime.date.today()
		today = '{today.month}/{today.day}/{today.year}'.format(today=today)
		for name in names:
			new_name = name[0].upper() + name[1:].lower()
			new_amount="%.2f"%(amounts[i])
			new_msg=message.format(
			name=new_name,
			date=today,
			amount=new_amount
			)
			i+=1
			print(new_msg)
			print('\n')

print_message(def_names,def_amts)
