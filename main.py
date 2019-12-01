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
import numpy as np

REF_STRING = None

def FIFO(num_frames: int):
    """
    First In First Out page replacement
    """
    memory = []

    fifo_q = queue.Queue(num_frames)
    page_fault_count = 0

    for x in REF_STRING:

        print('\n' + str(x) + ' on deck')
        show_rec(memory)
        show_queue(fifo_q)

        if x not in memory:  #page fault
            print('\npage fault ->', end=' ')
            page_fault_count += 1

            if not fifo_q.full(): #memory not full append value
                print('filling memory')
                fifo_q.put(x)
                memory.append(x)
                show_rec(memory)

            elif fifo_q.full():  #memory is full, use algorithm
                old = fifo_q.get()
                print('[removing ' + str(old) + ']')
                for i, item in enumerate(memory):
                    if item == old:
                        memory[i] = x
                        fifo_q.put(x)

                show_rec(memory)

        else:  #no page fault
            print('\nvalue found in memory(no fault)\t\t\t', end=' \n')
            show_rec(memory)

    print('\n\nTotal page faults: ', page_fault_count)

    return 0

def LRU(num_frames: int):
    """
    Least Recently Used page replacement
    """
    memory = []
    age = []

    #tracker = -1
    page_fault_count = 0

    for x in REF_STRING:
        #tracker += 1
        #if tracker == (num_frames):
         #   tracker = 0

        print('\n' + str(x) + ' on deck')
        print('Memory: ', *memory)
        print('Age:    ', *age)
        #print('tracker = ', tracker, end=' ')

        if x not in memory:  #page fault
            print('page fault ->', end=' ')
            page_fault_count += 1

            if len(memory) != num_frames: #memory not full append value
                print('filling memory')
                memory.append(x)
                age.append(0)
                age = [item + 1 for item in age]
                print('Memory: ', *memory)

            elif len(memory) == num_frames:  #memory is full, use algorithm
                index = age.index(max(age))
                print('[removing ' + str(memory[index]) + ']')
                memory[index] = x
                age = [item + 1 for item in age]
                age[index] = 0
                print('Memory: ',*memory)

        else:  #no page fault

            print('\nvalue found in memory(no fault)\t\t\t', end=' \n')
            age = [item + 1 for item in age]
            print('Memory: ', *memory)

    print('\n\nTotal page faults: ', page_fault_count)

    return 0


def OPT(num_frames: int):
    """
    Optimal page replacement
    """
    frame_age = []
    memory = []

    fifo_q = queue.Queue(num_frames)
    page_fault_count = 0

    for x in REF_STRING:

        print('\n' + str(x) + ' on deck')

        if x not in memory:  # page fault
            print('page fault\n', end='')
            page_fault_count += 1
            fifo_q.put(x)
            memory.append(x)
            show_rec(memory)

            if fifo_q.full():
                old = fifo_q.get()
                print('\t[removing ' + str(old) + ']')
                memory.remove(old)

        else:  # not page fault
            print('value found in memory(no fault)\t\t\t', end=' \n')
            show_rec(memory)
    return 0


def make_ref_string():
    """
    make a reference string of 100 random numbers between 0-49
    """
    ref = []
    for n in range(0, 100):
        ref.append(random.randint(0, 49))
    return ref

def show_queue(q):
    print('queue:', end='  ')
    for item in q.queue:
        print(item, end=' ')

def show_age(record: []):
    """
    helper function for debugging
    """
    print('age:   ', end=' ')
    n = 1
    if len(record) == 0:
        print('- - - - ')
    for x in record:
        if n != len(record):
            print(x,'',end=" ")
        else:
            print(x)
        n += 1

def show_rec(record: []):
    """
    helper function for debugging
    """
    print('memory:', end=' ')
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
                        default=10,
                        required=False,
                        help='number of physical-memory page frames available')
    parser.add_argument('-alg',
                        type=int,
                        dest='algorithm',
                        default=2,
                        required=False,
                        help='Algorithm to test: [1,2,3] - FIFO, LRU, OPT')
    args = parser.parse_args()

    # create reference string
    global REF_STRING
    REF_STRING = make_ref_string()

    if (args.algorithm == 1):
        FIFO(args.frames)
    elif (args.algorithm == 2):
        LRU(args.frames)
    elif (args.algorithm == 3):
        OPT(args.frames)
    else:
        print("Invalid algorithm selection")

    return 0

if __name__ == "__main__":
    main()
