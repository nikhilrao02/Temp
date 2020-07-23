class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None

	def __str__(self):
		if self.name is None:
			return "animal:" + str(self.age)
		else:
			return "animal:"+str(self.name)+":"+str(self.age)

animal1 = Animal(12)

print(animal1)

class Cat(object):
	
	def __init__(self, age):
		self.age = age
		self.name = None

	def __str__(self):
		if self.name is None:
			return "animal:" + str(self.age)
		else:
			return "animal:"+str(self.name)+":"+str(self.age)