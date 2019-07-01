'''
write a code  will take  input as your name and greet you with
good morning , good evening , goodafter noon , good night as per the current time your system :
'''
import datetime

name=input("enter user name")
time=datetime.datetime.now().hour

#time=datetime.hour

print('present time is',time)

if(time >= 7 and time< 12):
	print("gud morning")
elif(time >= 12 and time < 16 ):
	print("gud after noon")
elif(time >= 16 and time <20):
	print("gid evening")
elif(time>=20 and time <=24 or time >=0 and time <7):
	print("gud night")

