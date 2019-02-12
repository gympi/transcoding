#!/usr/bin/python
import argparse

from task import task_execute, tasks_registry
from tasks import *


def main():
    parser = argparse.ArgumentParser(description='API для транскодирования файлов')

    work_arguments = parser.add_argument_group('work arguments')

    work_arguments.add_argument('--task', '-t',
                                dest='task',
                                type=str,
                                default=None,
                                help='Task name',
                                required=True,
                                nargs='?'
                                )

    # args = vars(parser.parse_args())
    args, rest = parser.parse_known_args()
    args = vars(args)

    if 'task' in args and not args['task']:
        print("Tasks list:")
        for k, v in tasks_registry.get().items():
            print("\t{}".format(v._name))
    else:
        task_execute(**args, args=rest)


if __name__ == "__main__":
    main()
