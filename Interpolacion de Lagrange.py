def IntLagr(x,y,z):
	
	c="f(x)="
	for i in range(0, len(x)):
		d=""
		for j in range(0,len(x)):		
			if i==j:
				pass
			else:
				d+="(x-{})".format(x[j])
				pass
			pass
		e=""
		for j in range(0,len(x)):		
			if i==j:
				pass
			else:
				e+="({})".format(x[i]-x[j])
				pass
			pass
		if i==0:
			c+="{}*".format(y[i])+"[{}]".format(d)+"/[{}]".format(e)	
			pass		
		else:
			c+="+{}*".format(y[i])+"[{}]".format(d)+"/[{}]".format(e)
			pass
		pass
	print(c)
	a=0
	for i in range(0, len(x)):
		b=1
		for j in range(0,len(x)):		
			if i==j:
				b*=1
				pass
			else:
				b*=(z-x[j])/(x[i]-x[j])
				pass
			pass
		a+=y[i]*b	
		pass
	t="f({})=".format(z)+"{}".format(a)
	print(t)
	pass
def Inter_Lagrange():
	x=[]
	y=[]
	numec=input("Itroduzca la cantidad de coordenadas:")
	numec=int(numec)
	for l in range(0,numec):
		print("Introduzca la coordenada {}: ".format(l+1))
		corx=input("		x: ")
		corx=float(corx)
		x.append(corx)
		cory=input("		y: ")
		cory=float(cory)
		y.append(cory)
		pass
	z=input("Introduzca el valor en el cual quiere evaluar la funcion: ")
	z=float(z)
	IntLagr(x,y,z)
	pass
Inter_Lagrange()
