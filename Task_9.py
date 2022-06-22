'''
Необходимо создать два параллельных потока, каждый из которых выводил бы на экран числа от 10 до 1 в обратном
порядке с интервалом в одну секунду.
В выводе должно быть понятно какая нить выполняется, и когда каждая из них начинает и заканчивает своё выполнение.
'''

import threading
import time

class ClockThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        for x in range(10,0,-1):
            thread_name = threading.current_thread().name
            print(thread_name, x)
            time.sleep(1)

one = ClockThread()
two = ClockThread()
one.start()
two.start()
one.join()
two.join()