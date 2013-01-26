from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob




def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)

#square(bob,132)

def polygon(t,length,n):
	for i in range(n):
		fd(t,length)
		lt(t,float(float(360)/float(n)))

polygon(bob,100,8)
wait_for_user()
