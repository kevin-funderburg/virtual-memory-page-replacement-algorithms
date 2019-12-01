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

    print("First in first out")
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

    print('Least recently used page replacement')
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
            page_fault_count += 1
            print('page fault ->', end=' ')

            if len(memory) != num_frames: #memory not full append value
                print('filling memory')
                memory.append(x)
                age.append(0)
                age = [item + 1 for item in age]
                print('Memory: ', *memory)
                print('Page faults:', page_fault_count)

            elif len(memory) == num_frames:  #memory is full, use algorithm
                index = age.index(max(age))
                print('[removing ' + str(memory[index]) + ']')
                memory[index] = x
                age = [item + 1 for item in age]
                age[index] = 0
                print('Memory: ',*memory)
                print('Page faults:', page_fault_count)

        else:  #no page fault
            print('value found in memory(no fault)\t\t\t', end=' \n')
            age = [item + 1 for item in age]
            index = memory.index(x)
            age[index] = 0
            print('Age:    ', *age)
            print('Memory: ', *memory)

    print('\n\nTotal page faults: ', page_fault_count)

    return 0

def OPT(num_frames: int):
    """
    Optimal page replacement
    """

    print('Optimal page replacement')
    print("reference string length:", len(REF_STRING))
    print("Reference String: length["+ str(len(REF_STRING)) +']',*REF_STRING)

    age = []
    memory = []
    #distance = [] #corresponds to memory, each value represents the time until its memory value will be used

    page_fault_count = 0
    counter = -1

    for x in REF_STRING:
        counter += 1
        print('\n' + str(x) + ' on deck')
        print('Memory:', *memory)

        if x not in memory:  # page fault
            print("Reference String: length[" + str(len(REF_STRING)) + ']', *REF_STRING)
            page_fault_count += 1
            print('page fault ->', end=' ')

            if len(memory) != num_frames: # memory not full append value
                print('filling memory')
                memory.append(x)
                age.append(0)
                age = [item + 1 for item in age]
                print('Memory:', *memory)
                print('Page faults:', page_fault_count)

            elif len(memory) == num_frames: # memory is full use algorithm
                largest_ref_index = 0
                found = False
                removed = 0
                for mem_item in memory:
                    for ref_item in REF_STRING:
                        if mem_item == ref_item: #if mem_item is further down ref_string
                            found = True
                            if REF_STRING.index(ref_item) > largest_ref_index:
                                largest_ref_index = REF_STRING.index(ref_item)

                for item in memory: #replace item in memory
                    if item == REF_STRING[largest_ref_index]:
                        removed = item
                        memory[memory.index(item)] = x

                print('Age:    ', *age)
                if found == False: #if the item is no longer in the reference sting, replace oldest one
                    index = age.index(max(age))
                    print('[removing ' + str(memory[index]) + ']')
                    memory[index] = x
                    age = [item + 1 for item in age]
                    age[index] = 0

                print('ref string:', REF_STRING[largest_ref_index], 'at index: ', largest_ref_index)
                print('[removing ' + str(removed) + ']')
                print('Memory:',*memory)

        else:  # not page fault
            print('value found in memory(no fault)\t\t\t', end=' \n')
            print('Memory:',*memory)
            
        REF_STRING[counter] = 50

    print('\n\nTotal page faults: ', page_fault_count)

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
                        default=5,
                        required=False,
                        help='number of physical-memory page frames available')
    parser.add_argument('-alg',
                        type=int,
                        dest='algorithm',
                        default=3,
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
