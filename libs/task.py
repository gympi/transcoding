import time
from functools import reduce

from libs.arguments import argparse_adapter


class TaskRegistry:
    def __init__(self):
        self._tasks_registry = dict()

    def exist(self, key, **kwargs):
        return key in self._tasks_registry

    def get(self, key=None):
        if key is None:
            return self._tasks_registry
        elif self.exist(key):
            return self._tasks_registry[key]
        else:
            raise Exception('Can not find task "{}".'.format(key))

    def add(self, key, task):
        if self.exist(key):
            raise Exception('Task "{}" exist.'.format(key))

        if not isinstance(task, TaskWraper):
            raise Exception('Task "{}" does not implement interface "TaskWraper"'.format(key))

        self._tasks_registry[key] = task


def seconds_to_str(t):
    return "%d:%02d:%02d.%03d" % \
           reduce(lambda ll, b: divmod(ll[0], b) + ll[1:],
                  [(t * 1000,), 1000, 60, 60])


class TimeExecute:
    def __init__(self):
        self._begin = 0
        self._end = 0
        self._time = 0

    def begin(self):
        self._begin = time.time()

    def end(self):
        self._end = time.time()
        self._time = time.time() - self._begin

    def __str__(self):
        return self._time

    def __repr__(self):
        return self.__str__()


class Task:
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def __call__(self, func):
        return TaskWraper(func, *self._args, **self._kwargs)


class TaskWraper:
    def __init__(self, func, name=None, validator=None, *args, **kwargs):
        self._func = func
        self._name = name
        self._validator = validator
        self._time_execute = TimeExecute()
        self._registry()

    def _registry(self):
        tasks_registry.add(self._name, self)

    def _before_execute(self):
        self._time_execute.begin()

    def _after_execute(self):
        self._time_execute.end()

    def __call__(self, *args, **kwargs):
        self._before_execute()

        func_data = self._func(*args, **kwargs)

        self._after_execute()
        return func_data


def task_execute(task, args):
    args = argparse_adapter(tasks_registry.get(task)._validator).parse_args(args)
    tasks_registry.get(task)(**vars(args))


task = Task
tasks_registry = TaskRegistry()
