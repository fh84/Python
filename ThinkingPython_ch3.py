### chapter 3
import math 
print math

radians=0.7
height=math.sin(radians) # sin, cosin fcts take radians as unit

#from degrees to radians
degrees=45
radians=(degrees/360.0)*2*math.pi
print math.sin(radians)
print height

def print_lyrics():
	print "I'm a lumberjack, and I'm okay!"
	print "I sleep all night and I work all day"


print print_lyrics
print_lyrics()

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

repeat_lyrics()


def print_twice(florian):
	print florian
	print florian

print_twice("Skitty")

def cat_twice(part1,part2):
	cat =part1+part2
	print_twice(cat)

line1='Bing tiddle'
line2='tiddle bang.'

cat_twice(line1,line2)


def do_twice(func):
	func()
	func()

def print_spam():
	print "spam"

do_twice(print_spam)

### excercise grid

def do_four(fnc):
	do_twice(fnc)
	do_twice(fnc)

def print_beam():
	print '+ - - -',

def print_post():
	print '|      ',

def one_row():
	do_four(print_beam)
	print '+'
	do_four(print_post)
	print '|'
	do_four(print_post)
	print '|'
	do_four(print_post)
	print '|'
	do_four(print_post)
	print '|'

def print_grid():
	do_four(one_row)
	do_four(print_beam)
	print '+'

print_grid()		
	

