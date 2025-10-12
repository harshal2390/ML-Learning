import threading
import time

def print_nums():
    for i in range(5):
        time.sleep(2)
        print(f"nums:{i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")

# create 2 threads
t1=threading.Thread(target=print_nums)
t2=threading.Thread(target=print_letters)


t=time.time()
t1.start()
t2.start()

## wait for threads to cmplete 
t1.join()
t2.join()
finised_time=time.time()-t
print(finised_time)