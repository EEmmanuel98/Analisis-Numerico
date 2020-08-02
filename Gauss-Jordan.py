import numpy as np
def GaussJordan (z) :
	m=0
	dgpx=[]
	var=[]
	g=0
	for g in range(1,len(z[0])): #se genera una lista con el numero el nombre de las variables
		var.append("x_{}".format(g))
		pass
	for col in range(0,len(z[0])-1):
		for fil in range(col-m,len(z)):
			k=0
			b = z [fil][col] 
			if b != 0: #buscamos un elemento distinto de cero en la columna
				dgpx.append(col) #cadena que contiene a la diagonal principal 
				aux= []        #cambio de lugar de la primera fila con un elemento distinto de cero en la columna en la que estamos trabajando a la pocicion adecuada
				aux = z [fil]
				z[fil] = z[col-m]
				z[col-m] = aux
				aux=[]
				for x in range(0,len(z[0])): #division por el elemento de la diagonal principal
					aux.append(z[col-m][x]/b)
					pass
				z[col-m]=aux
				for y in range(0,len(z)):	#hacemos ceros los demas numeros de la columna
					if col-m != y:
						aux=[]
						for x in range(0,len(z[0])):
							aux.append(z[y][x]-z[y][col]*z[col-m][x])
							pass
						z[y]=aux
						pass
					pass
				pass			
			else:
				k=k+1 #conteo de cuantos ceros hay en la columna
				pass
			if (k== len(z)-col+m): #si estamos en una columna de ceros se omite 
				m=m+1
				pass	
			pass
		pass
	t=0
	print(np.array(z))
	if len(z)>=len(z[0])-1: #cuando la matriz es cuadrada o tiene mas filas que columnas
		for n in range(0,len(z[0])-1):
			if z[n][n]==0: #buscamos si hay una fila de ceros 
				if z[n][-1]!=0: #si esta igualada a un valor diferente a cero se dice que no tiene solucion
					print("El sistema no tiene solución")
					return 	
				t=+1 #contador si encontramos un cero en la diagonal principal
				pass
			pass
		for x in range(len(z[0])-1,len(z)): #buscamos filas de ceros abajo de la diagonal principal
			if z[x][-1]!=0: #si estan igualados a un valor diferente a cero se dice que no tiene solucion
				print("El sistema no tiene solución")
				return
			pass
		if t>0: #si se encontro un cero en la diagonal principal se dice que tiene soluciones infinitas
			print("El sistema tiene soluciónes infinitas")
			for a in dgpx: #valores en donde la diagonal principal es distinta a cero
				sol="" 
				for b in range(0,len(z)):
					if z[b][a] == 1:
						sol=sol+"{}".format(var[a])+"={}".format(z[b][-1]) #igualamos la variable con la constante 
						for c in range(a+1,len(z[0])-1):	
							if z[b][c]!=0:
								sol=sol+"+{}".format(-z[b][c])+"{}".format(var[c]) #"despejamos" los demas valores 
								pass
							pass
						print(sol) #imprimimos el valor dependiente de la variable
						pass
					pass
				pass
			pass
		else:
			print("El sistema tiene solucion unica")
			for a in dgpx: #omitimos si se encuentra una columa de ceros 
				for b in range(0,len(z)):
					if z[b][a] == 1: #buscamos en que fila esta la variable
						print("{}".format(var[a])+"={}".format(z[b][-1])) #imprimimos el valor de la variable 
						pass
					pass
				pass
			pass
		pass	
	else: #si hay mas variables que ecuaciones
		print("El sistema tiene soluciónes infinitas")
		for a in dgpx: #
			sol=""
			for b in range(0,len(z)): #buscamos en que fila se ecuentra la variable 
				if z[b][a] == 1:
					sol=sol+"{}".format(var[a])+"={}".format(z[b][-1]) #la igualamos a la constante
					for c in range(a+1,len(z[0])-1):	
						if z[b][c]!=0:
							sol=sol+"{}".format(-z[b][c])+"{}".format(var[c]) #"despejamos" la variable 
							pass
						pass
					print(sol) #imprimimos el valor dependiente de la variable
					pass
				pass
			pass
		pass
	pass
def Gauss_Jordan():
	z=[]
	numec=input("Itroduzca el numero de ecuaciones:")
	numec=int(numec)
	vari=input("Itroduzca el numero de variables:")
	vari=int(vari)
	for x in range(0,numec):
		print("Ec{}: ".format(x+1))
		ec=[]
		for y in range(0,vari):
			cof=input("	Coeficiente de la variable {}: ".format(y+1))
			cof=float(cof)
			ec.append(cof) #formamos la lista de la ecuacion
			pass
		cof=input("	contstante de la ecuacion {}: ".format(x+1))	
		cof=float(cof)
		ec.append(cof) #agregamos la constante 
		z.append(ec) #formamos la lista de las ecuaciones
		pass
	GaussJordan(z)
	pass
Gauss_Jordan()