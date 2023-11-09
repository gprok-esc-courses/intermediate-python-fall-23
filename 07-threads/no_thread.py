import datetime
import time
import random


def counter(task_id):
    for i in range(10):
        print(task_id, ": ", i)
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    start = datetime.datetime.now()
    for task in range(5):
        counter(task)
    end = datetime.datetime.now()
    print("Completed!", end-start)
