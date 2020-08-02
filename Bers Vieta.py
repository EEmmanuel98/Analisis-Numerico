def BergeVieta (z):
	if len(z)==1:
		print ("No es un polinomio, por tanto no es factorizable")
		return
		pass
	elif z[-2]==0 :
		print ("No se pueden encontrar raices por este metodo ya que el coeficiente de el termino lineal es 0" ) 
		return
		pass 
	elif len(z)==2:
		print ("P(x)={}".format(z[0])+"x+{}".format(z[1]))
		return
	else:
		u=[]
		r=len(z)
		for x in range(1,r):
			y=-z[-1]/z[-2]
			q=0
			t=[z[0]]
			while q<200 and t[-1]!=0:
				t=[z[0]]
				for i in range(0,len(z)-1):
					w=z[i+1]+t[i]*y
					t.append(w)	
					pass
				k=[t[0]]
				for i in range(0,len(t)-2):
					v=t[i+1]+k[i]*y
					k.append(v)
					pass
				y=y-(w/v)
				q=1+q
				pass
			if t[-1]==0:
				u.append(y)
				pass

			else:
				irras=""
				for i in range(0,len(z)-1):
					irras=irras+"{}".format(z[i])+"x^{}".format(len(z)-i-1)+"+"
					pass
				irras=irras+"{}".format(z[-1])
				ras=""
				for i in range(0,len(u)):
					ras="(x-{}".format(u[i])+")"+ras
					pass
				print("P(x)=("+irras+")"+ras)
				return
				pass 
			z=[]
			for j in range(0,len(t)-1):
				z.append(t[j])
				pass
			if len(z)==2:
				irras="x+{}".format(z[-1]/z[0])
				ras=""
				for i in range(0,len(u)):
					ras="(x-{}".format(u[i])+")"+ras
					pass
				print("P(x)=("+irras+")"+ras)
				return
				pass
			elif z[-3]==0:
				irras=""
				for i in range(0,len(z)-1):
					irras=irras+"{}".format(z[i])+"x^{}".format(len(z)-i-1)+"+"
					pass
				irras=irras+"{}".format(z[-1])
				ras=""
				for i in range(0,len(u)):
					ras="(x-{}".format(u[i])+")"+ras
					pass
				print("P(x)=("+irras+")"+ras)
				return
				pass  
			pass
		pass
	pass
def Berge_Vieta():
	z=[]
	numec=input("Itroduzca la potencia del polinomio P(x):")
	numec=int(numec)
	for y in range(0,numec):
		cof=input("	Introduzca el coeficiente de x^{}: ".format(numec-y))
		cof=float(cof)
		z.append(cof)
		pass
	cof=input("	Introduzca la constante: ")
	cof=float(cof)
	z.append(cof)
	BergeVieta(z)
	pass
Berge_Vieta()
