#!/usr/bin/python
import argparse

from task import task_execute
from tasks import *


def main():
    parser = argparse.ArgumentParser(description='API для транскодирования файлов')

    parser.add_argument('--task', '-t',
                        type=str,
                        dest='task',
                        help='Task name')

    parser.add_argument('--input', '-i',
                        type=str,
                        dest='input',
                        help='Input file path')

    parser.add_argument('--output', '-o',
                        type=str,
                        dest='output',
                        help='Output file path')

    args = parser.parse_args()

    task_execute(**vars(args))


if __name__ == "__main__":
    main()
