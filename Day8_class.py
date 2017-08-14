#Positional and Keyword Arguments
def printrainy(arg1,arg2,karg1="Sunny",karg2="Day"):
	if karg1!= "Sunny":
		print(arg1+" "+arg2+" "+karg1+" "+karg2)
	else:
		print("Not Rainy")

printrainy("It","is","Rainy")
printrainy("It","is")

#Class Animal
class Animal():
	name="Brutus"
	noise='grunt'
	size='large'
	color='brown'
	def get_color(self):
		return self.color
	@property
	def get_noise(self):
		return self.noise

#Class Dog inhertited class Animal
class Dog(Animal):
	name='Tommy'
	noise='bark'

	def get_color(self):
		return self.color


dog=Dog() 
print(dog.get_color())
print(dog.get_noise)
