print("Fecha")
a=int(input('Escribe el dia: '))
b=int(input('Escribe el mes: '))
c=int(input('Escribe el año: '))
if a>0 and b>0 and c>0:
	if (b<=12 and a<=31) and ((b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12) and a<=31) or ((b==4 or b==6 or b==9 or b==11) and a<=30) or (a<=29 and b==2 and c%4==0) or (a<=28 and b==2 and c%4!=0):
		a=a+1
		if (b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12) and a==32:
				a=1
				b=b+1
				if b==13:
					b=1
					c=c+1
		if (b==4 or b==6 or b==9 or b==11) and a==31:
				a=1
				b=b+1
		if a==30 and b==2 and c%4==0:
				a=1
				b=b+1
		if a==29 and b==2 and c%4!=0:
				a=1
				b=b+1
		print("El dia siguiente es: ",a,"/",b,"/",c)						
	else:
		print("Fecha inválida")
	  

