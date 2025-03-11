import time

class Clock:
    def c_func(self):
        try:
            while True:
                present = time.localtime()
                res = time.strftime("%H:%M:%S %p",present)
                print(res)
                time.sleep(2)

        except KeyboardInterrupt:
            print("Stop the Clock")


C = Clock()
C.c_func()