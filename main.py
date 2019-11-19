##
# @authors Kevin Funderburg
#
# Created on 11/19/19
#


from collections import deque
import random
import argparse


def FIFO(num_frames: int):
    # something
    return 0


def LRU(num_frames: int):
    # something
    return 0


def OPT(num_frames: int):
    # something
    return 0


def make_ref_string(length: int, max: int):
    # refString = NONE
    ref = []

    for n in range(0, 100):
        ref.append(random.randint(0, 49))

    return ref


def main():
    # build argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=int, required=True,
                        help='number of physical-memory page frames available')
    parser.add_argument('-a', type=int, required=False, help='Algorithm to test:'
    args = parser.parse_args()

    ref_string = make_ref_string(1, 5)
    for x in ref_string:
        print(x)

    return 0


if __name__ == "__main__":
    main()