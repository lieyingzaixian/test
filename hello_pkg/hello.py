# hello1.py

__main__ = 'This is hello_pkg package.'

if __name__ == 'hello':
	print('hello_pkg package hello module load success.')

def phello(value='Hello, world!'):
	print('hello module value of :',value)

def multiply(x=0, y=0):
	return (x * y)



