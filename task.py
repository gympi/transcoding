import time
from functools import wraps, reduce

tasks_registry = dict()


class TaskOld:
    def __init__(self, name=None):
        self._name = name
        self.time_execute = 0

    def __call__(self, func):
        if not self._name:
            self._name = func.__name__

        c = wraps(func)

        def wrapped_func(*args, **kwargs):
            t0 = time.time()
            func_data = func(*args, **kwargs)
            self.time_execute = t0 - time.time()

            return func_data

        return wrapped_func


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
    def __init__(self, func, name=None, *args, **kwargs):
        self._func = func
        self._name = name
        self._time_execute = TimeExecute()
        print('init')
        self._registry()

    def _registry(self):
        tasks_registry.update({self._name: self})

    def _before_execute(self):
        self._time_execute.begin()

    def _after_execute(self):
        self._time_execute.end()

    def __call__(self, *args, **kwargs):
        print('run decorator')
        self._before_execute()

        func_data = self._func(*args, **kwargs)

        self._after_execute()
        return func_data


task_old = TaskOld
task = Task


def exist_task(task, **kwargs):
    print(task)
    return task in tasks_registry


def task_execute(task, **kwargs):
    if task in tasks_registry:
        task = tasks_registry.get(task)
        print(task)
        task(**kwargs)
