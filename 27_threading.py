from threading import *
from time import sleep


class Hi(object):
  # class level variable self mandatory?
    def run(self):
        i = 0
        while i <= 5:
            # print("Hi")
            i += 1


class Hello(object):
  # class level variable self mandatory?
    def run(self):
        i = 0
        while i <= 5:
            # print("Hello")
            i += 1


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

print()


class HiThread(Thread):
  # class level variable self mandatory?
    def run(self):
        i = 0
        while i <= 4:
            sleep(1)
            print("Hi")
            i += 1


class HelloThread(Thread):
  # class level variable self mandatory?
    def run(self):
        i = 0
        while i <= 4:
            sleep(1)
            print("Hello")
            i += 1


t3 = HelloThread()
t4 = HiThread()

# Will not work
# t3.run()
# t4.run()

# We need start
# run compulsory
# some time output HiHello
# cpu
t3.start()
t4.start()
# main thread
# not prints at end
# to print at end, wait main thread
t3.join()
t4.join()
print("Bye")
