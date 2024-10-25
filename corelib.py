#core library 
# pre-installed modules- 
# import glob 
# lst = glob.glob("*")
# print (lst)

#split shortcut do all 4 split (remove delimeter)
# import re 
# data = "10-20,30:40;50"
# res = re.split(r"[\-,:;]",data)
# print (res)

#Debug python
#debugger - apply break points/stepinto,stepover,stepout
#documentation - triple quotes
#unittest - unittest
#how to install module -  pip install bs4
#                         pip uninstall bs4
#                         pip install -- upgrade bs4
#                         pip list
#how to dist              - setuptools / distutils
# def add(num1,num2):
#     num1 = num1 +5
#     num2 = num2 +3
#     ans = num1 + num2
#     return ans 
# a =10 
# b = 20 
# res = add(a,b)
# print(res)

#-------------------threads , asyncio , process ------------------------
# 
# 
# 
# 
# -
# import threading 
# def job1():
#     print("job1")

# def job2():
#     print("job2")
# if __name__=="__main__":
#     t1 = threading.Thread(target=job1)
#     t2 = threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


# import threading 
# import os
# def job1():
#     print("job1 =",os.getpid())

# def job2():
#     print("job2 =",os.getpid())
# if __name__=="__main__":
#     t1 = threading.Thread(target=job1)
#     t2 = threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# multiprocess

import multiprocessing
import os

def job1():
    print("Job1 =",os.getpid())

def job2():
    print("Job2 =",os.getpid())
if __name__=="__main__":
    print("Main = ",os.getpid())
    P1 = multiprocessing.Process(target=job1)
    P2 = multiprocessing.Process(target=job2)
    P1.start()
    P2.start()
    


