class employee:
	def __init__(self,a,n,sal,dept,desig):
		self.a=a
		self.nm=n
		self.salary=sal
		self.dept=dept
		self.desig=desig
	def show(self):
		print("employee expericience=",self.a)
		print("employee name=",self.nm)
		print("employee salary=",self.salary)
		print("employee department=",self.dept)
		print("employee designation=",self.desig)
e=employee(101,"bindia",90000,"IT","Devoloper")
e.show()
e1=employee(202,"payal",45000,"IT","trainee")
e1.show()