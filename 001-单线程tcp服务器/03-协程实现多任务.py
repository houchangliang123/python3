import time

def A():
	while True:
		print("_______A______")
		yield
		print("______A1______")
		time.sleep(0.5)



def B(c):
	while True:
		print("______B______")
		c.__next__()
		print("______B1______")
		time.sleep(0.5)


if __name__=='__main__':
	a = A()
	B(a)
