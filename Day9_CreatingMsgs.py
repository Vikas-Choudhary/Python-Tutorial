import datetime

class MessageUser():
    user_Details =[]
    messages=[]
    base_message= """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purchase total was Rs {total}.
"""
    def add_user(self,name,amount,email=None):
        name = name[0].upper() + name[1:].lower()
        amount="%.2f"%(amount) 
        detail={
        "name": name,
        "amount":amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        if email is not None:
            detail['email']=email
        detail['date']= date_text
        self.user_Details.append(detail)

    def get_details(self):
        return self.user_Details

    def make_messages(self):
        if len(self.user_Details) >0:
            for detail in self.get_details():
                name=detail["name"]
                amount=detail["amount"]
                date=detail['date']
                nmessage=self.base_message.format(
                    name=name,
                    date=date,
                    total=amount)
                self.messages.append(nmessage)
            return self.messages
        return[]

    def print_messages(self):
        self.make_messages()
        for msg in self.messages:
            print(msg)
 
obj=MessageUser()
obj.add_user("Saurabh",1250)
obj.add_user("veronica",7600)
obj.add_user("sid",3500)
#print(obj.get_details())

#print(obj.make_messages())
obj.print_messages()

#new_name=input("Enter the name ")
#new_amount=int(input("Enter the amount "))
#obj.add_user(new_name,new_amount)
#print(obj.get_details())

