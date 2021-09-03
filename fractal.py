from turtle import*
from random import*

left(90)
branch_len = 100
angle = 30
speed(100)
pencolor('brown')

def branch(branch_len,angle):
	angle = randint(20,35)
	sf = uniform(0.55,0.82)
	pensize(branch_len/10)
	if branch_len <10:
		pencolor('green')
		stamp()
		pencolor('brown')
		return
	else:
		forward(branch_len)
		left(30)
		branch(sf*branch_len,angle)
		right(60)
		branch(sf*branch_len,angle)
		left(30)
		backward(branch_len)

branch(120,30)