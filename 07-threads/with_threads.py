import datetime
import time
import random
import threading


def counter(task_id):
    for i in range(10):
        print(str(task_id) + ": " + str(i) + "\n", end='')
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    start = datetime.datetime.now()
    threads = []
    for task in range(5):
        th = threading.Thread(target=counter, args=(task,))
        threads.append(th)
        th.start()
    for th in threads:
        th.join()
    end = datetime.datetime.now()
    print("Completed!", end-start)