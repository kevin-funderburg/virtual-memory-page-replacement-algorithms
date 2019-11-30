##
# @authors Kevin Funderburg
#
# Created on 11/19/19
#

from collections import deque
import queue
#import logging
import random
import argparse
#import matplotlib.pyplot as plt
#import numpy as np

REF_STRING = None

def FIFO(num_frames: int):
    """
    First In First Out page replacement
    """
    record = []
    fifo_q = queue.Queue(num_frames)
    page_fault_count = 0

    for i in REF_STRING:
        x = int(i)
        print('\t' + str(x) + ' on deck')

        if x not in record: #page fault
            print('page fault\t\t\t', end=' ')
            page_fault_count += 1
            fifo_q.put(x)
            record.append(x)
            show_rec(record)

            if fifo_q.full():
                old = fifo_q.get()
                print('\t[removing ' + str(old) + ']')
                record.remove(old)

        else:   # not page fault
            print('not page fault\t\t\t', end=' ')
            show_rec(record)

    print('\nTotal Faults: ' + str(page_fault_count))
    return 0


def LRU(num_frames: int):
    """
    Least Recently Used page replacement
    """
    # TODO
    return 0


def OPT(num_frames: int):
    """
    Optimal page replacement
    """
    # TODO
    return 0


def make_ref_string():
    """
    make a reference string of 100 random numbers between 0-49
    """
    ref = []
    for n in range(0, 100):
        ref.append(random.randint(0, 49))
    return ref

def show_rec(record: []):
    """
    helper function for debugging
    """
    n = 1
    if len(record) == 0:
        print('- - - - ')
    for x in record:
        if n != len(record):
            print(x, end=" ")
        else:
            print(x)
        n += 1

def main():
    # build argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames',
                        type=int,
                        dest='frames',
                        default=3,
                        required=False,
                        help='number of physical-memory page frames available')
    parser.add_argument('-a',
                        type=int,
                        required=False,
                        help='Algorithm to test: [1,2,3] - FIFO, LRU, OPT')
    args = parser.parse_args()

    # create reference string
    global REF_STRING
    REF_STRING = make_ref_string()

    frames = 3
    FIFO(args.frames)
    return 0


if __name__ == "__main__":
    main()
