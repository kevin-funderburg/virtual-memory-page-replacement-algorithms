##
# @authors Kevin Funderburg
#
# Created on 11/19/19
#

from collections import deque
import queue
import logging
import random
import argparse

REF_STRING = None

def FIFO(num_frames: int):
    record = []
    fifo_q = queue.Queue(num_frames)


    for x in REF_STRING:

        if x not in record:
            print('page fault\t\t\t', end=" ")
            fifo_q.put(x)
            record.append(x)

            show_rec(record)

            if fifo_q.full():
                old = fifo_q.get()
                print('[removing ' + str(old) + ']')
                record.remove(old)

        else:
            print('not page fault\t\t\t', end=" ")
            show_rec(record)




    return 0

def show_rec(record: []):
    if (len(record) == 0):
        print('- - - - ', end=" ")
    for x in record:
        print(x, end=" ")

def LRU(num_frames: int):
    # something
    return 0


def OPT(num_frames: int):
    # something
    return 0


def make_ref_string(length: int, max: int):
    ref = []
    for n in range(0, 100):
        ref.append(random.randint(0, 49))
    return ref


def main():
    # build argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames',
                        type=int,
                        dest='frames',
                        required=True,
                        help='number of physical-memory page frames available')
    parser.add_argument('-a',
                        type=int,
                        required=False,
                        help='Algorithm to test: [1,2,3] - FIFO, LRU, OPT')
    args = parser.parse_args()

    # create reference string
    global REF_STRING
    REF_STRING = make_ref_string(1, 5)

    FIFO(4)
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()