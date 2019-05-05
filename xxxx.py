import threading
import time

def fun1():
   i = 0
   while True:
      with open('a.txt', 'a+') as f1:
         f1.write("%s\n" % i)
         i = i + 1
         time.sleep(1)

def fun2():
   while True:
      with open('a.txt','r') as f2:
         print(f2.readlines())
         time.sleep(2)



threads = []
threads.append(threading.Thread(target=fun1))
threads.append(threading.Thread(target=fun2))

if __name__ == '__main__':
   for t in threads:
      print(t)
      t.start()