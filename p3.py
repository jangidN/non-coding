adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
'''
print("print only those numbers greater than 5
also print those numbers those are less than or  equals to 2  ( <= 2 )
store these answers in in two different list also")'''
a=[]
b=[]
for i in adhoc:
	if(i>5):
		a.append(i)
	elif(i<=2):
		b.append(i)

print("no. greater than 5 are ",a)
print("no. greater than 5 are ",b)
