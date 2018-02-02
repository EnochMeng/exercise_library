# 如何创建线程
import threading
import time

def foo(n):
    print('%s' % n)


t1 = threading.Thread(target=foo, args=(1,))
t1.start()


# 上面就是直接创建了一个子线程t1

# 下面讲一个使用类进行创建子线程，以后要常用这个来创建子线程
class Mythread(threading.Thread):

    def __init__(self, n):
        threading.Thread.__init__(self)
        self.num = n

    def run(self):  # 这个run重写了父类中的run方法，把你要运行的子线程函数写在这个里面，就是相当于把上面的foo方法写在这个里面
        print('%s' % self.num)


t2 = Mythread(2)
t3 = Mythread(3)
# 这里运用自己的类创建了两个子线程，其实就是继承了threading.Thread类，然后把要执行的写进去就ok了
# 这里就和上面一样调用了
t2.start()
t3.start()



# 同步锁threading.Lock
num = 100


def bar():
    global num  # 这个num是个外部变量，在这里我们不能修改num的值，所以要把num变成全局变量，下面的num -= 1就能执行了，不然下面那句执行不了
    # num -= 1
    # print('ok')
    r.acquire()  # 加上同步锁，不让cpu切换
    temp = num
    time.sleep(0.001)
    num = temp - 1  # 不加锁的情况下，这样执行，就会发现结果不是0了，因为cpu的执行在中途切换了，因此要在上下加上锁，保证cpu在执行这中间的数据操作时不能切换去执行其他的东西
    r.release()  # 解开同步锁


thread_list = []
r = threading.Lock()  # 创建一个锁

for i in range(100):
    t = threading.Thread(target=bar)
    t.start()

    thread_list.append(t)

for item in thread_list:  # 这里只所以写一个for循环，是为了保证所有子线程执行完后，再执行主线程，不然的话，下面的print()就会先打印出来，我们就看不到现象了。
    item.join()  # join的意思就是要等待这个线程执行完，才会去走其他线程。

print('result', num)

# 死锁现象，解决死锁现象得运用递归锁，r = threading.RLock(), 加个R就是递归锁，这个锁可以多次运用，内部有个计数器，就像是大门里面还有个小门。
# GIL限制一次只能有一个thread进入解释器执行，cpu在执行线程时会出现切换现象。
# 信号量semaphore = threading.BoundeSemaphore(5),这就创建信号量锁，这里的5参数表示同时可以进入的线程数量，比喻为停车场的车位有5个，同时只能停5个。
# 条件变量lock_con = threading.Condition(),这里就创建了条件标量锁，这把锁默认创建一种RLock锁，它有三个方法，wait()等待其他线程的通知,notify()通知其他线程,notifyall()通知其他所有线程
# 这里一共讲了4把锁，普通锁Lock，递归锁Rlock，信号量BoundeSemaphore，条件变量Condition，可以自己去详细了解这里都是讲了对线程进行加锁。
# 条件事件对象event = threading.Event()，创建一个事件对象，类似于条件变量，也是用来在线程之间传递状态条件，event.isSet()返回状态，event.set()设置为True,event.clear()设置为False，event.wait()如果isSet为False就将线程阻塞True就向下走。

# 队列，多线程利器，队列在多线程中使用数据很安全，他自己内部给数据上了锁，多线程操作时数据就不会乱。
import queue

d = queue.Queue(3)   # 3表示可以放几个数据，放三个。取出去一个，就可以接着放进去一个，放不下就会阻塞住
#  d = queue.Queue(3)
d.put('a')
d.put('b')
d.put('c')
#  d.put('c'，0)加个0，在队列满的情况下，再添加这个数据时，就会报错，告诉你满了
print(d.get())
print(d.get())
print(d.get())
print(d.get())   # 队列里的东西拿完了，这时候也阻塞，拿不出来
print(d.get(0))   # 加个0，取不到时，就会报错没东西取了
# 队列，先进先出，也可以调成先进后出，都是可以调的，put放进去，get拿出来。里面还有很多方法，可以自己去查看，队列在多线程非常有用。