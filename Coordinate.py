class coordinate:

	def __init__(self, x=1, y=1):

		self.x = x
		self.y = y

	def __str__(self):

		return "<" + "," + str(self.y) + ">"

	def distance(self, other):

		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5


point1 = coordinate(1,1)
point2 = coordinate(3,3)
print(point1.distance(point2))
print(coordinate.distance(point1,point2))

class cordinate:

	def __init__(self, x=1, y=2):

		self.x = x
		self.y = y

	def __str__(self):

		return "<" +str(self.x)+ ","+ str(self.y) + ">"

	def distance(self, other):
		
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5


point1 = coordinate(1,1)
point2 = coordinate(3,3)
print(point1.distance(point2))
print(coordinate.distance(point1,point2))

class Square:
	def __init__(self,side):
		self.side = int(side)
	def area(self):
		return (self.side)**2
	def diagonal(self):
		return (2*(self.side**2))**0.5
	def __str__(self):
		return f"Square of side {self.side}"



class Square:
	def __init__(self,side):
		self.side = int(side)
	def area(self):
		return (self.side)**2
	def diagonal(self):
		return (2*(self.side**2))**0.5
	def __str__(self):
		return f"Square of side {self.side}"

