import gevent
#多任务分为两种情况：
	#（1）计算密集型，例如（for的多层循环）在这种情况下python在开启多线程只有一个核心在工作，即使有是多核cpu也只有一个核心在工作。在这种情况下用该使用多进程
	#(2)  I/O密集型。例如（socket等待链接）在这种情况下比较适合多线程

#协程只要是在一个进程下的一个线程下多个协程这样在执行单个线程可以执行多任务的思想（利用一个线程在多个函数内进行跳转）
def f(n):
	for i in range(n):
		print(gevent.getcurrent(),i)
		#用来模拟一个耗时操作，gevent会自动切换协程(注意不是time模块下的sleep)
		gevent.sleep(1)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()
