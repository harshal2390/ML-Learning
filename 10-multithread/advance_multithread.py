from concurrent.futures import ThreadPoolExecutor
import time

#multithreading
""" def print_nums(nums):
    time.sleep(2)
    return f"nums: {nums}"

nums=[1,2,3,4,5,6,7,8,9,0,12,4]
with ThreadPoolExecutor(max_workers=4) as executor:
    t=time.time()
    results=executor.map(print_nums,nums)
finised_time=time.time()-t
print(finised_time)

for res in results:
    print(res) """

###  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)