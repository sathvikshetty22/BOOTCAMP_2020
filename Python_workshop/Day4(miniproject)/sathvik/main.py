from arith1 import add
from arith1 import sub
from arith1.arith2 import mul,div,mdiv
from relate1 import great,less
from relate1.relate2 import equal
loop=1
while loop==1:
	print("Enter the choice:")
	print("1.ADD")
	print("2.SUB")
	print("3.MUL")
	print("4.DIV")
	print("5.MODULUS")
	print("6.GREATER")
	print("7.LESSER")
	print("8.EQUAL")
	print("9.QUIT")
	choice=int(input())
	if choice==1:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		add.func(a,b)
	elif choice==2:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		sub.func(a,b)
	elif choice==3:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		x=mul.arith21()
		x.func(a,b)
	elif choice==4:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		x=div.arith22()
		x.func(a,b)
	elif choice==5:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		x=mdiv.arith23()
		x.func(a,b)
	elif choice==6:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		great.func(a,b)
	elif choice==7:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		less.func(a,b)
	elif choice==8:
		a=int(input("enter 1st number"))
		b=int(input("enter 2nd number"))
		x=equal.rel()
		x.func(a,b)
	else:
		loop=0
		print("THANK YOU")

		
		


