import os, time, random
from multiprocessing import Pool


def long_time(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time, args=(i, ))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocesses done.')