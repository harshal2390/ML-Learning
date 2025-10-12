 #parellel execution - multi cores of cpu 
import multiprocessing
import time

def square_nums():
    for i in range(5):
        time.sleep(3)
        print(f"sqaure:{i*i}")

def cube_nums():
    for i in range(5):
        time.sleep(3)
        print(f"cube:{i*i*i}")

if __name__=="__main__":
    p1=multiprocessing.Process(target=square_nums)
    p2=multiprocessing.Process(target=cube_nums)

    t=time.time()
    p1.start()
    p2.start()

    ## wait for threads to cmplete 
    p1.join()
    p2.join()
    finised_time=time.time()-t
    print(finised_time)