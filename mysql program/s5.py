class employee:
	def __init__(self,a,n,sal):
		self.a=a
		self.nm=n
		self.salary=sal
	def show(self):
		print("employee expericience=",self.a)
		print("employee name=",self.nm)
		print("employee salary=",self.salary)
s=employee(2,"bindia",90000)
s.show()