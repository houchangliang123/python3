from threading import Thread

def name():
	print("1")

def main():
	tr = Thread(target=name)
	tr.start()


if __name__ == "__main__":
	main()
