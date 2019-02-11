#!/usr/bin/python
import argparse
import json
import os.path
import yaml

from task import exist_task, task_execute
from tasks import *


class Task:
    def __init__(self, options, command, args):
        self._options = options
        self._command = command
        self._args = args


def workflow_run(workflow: str, **kwargs):
    print(workflow)
    if os.path.exists(workflow) and os.path.isfile(workflow):

        data = {}

        if workflow.endswith('.json'):
            with open(workflow, 'r') as stream:
                try:
                    data = json.load(stream)
                except json.JSONDecodeError as exc:
                    print(exc)
                    exit()

        elif workflow.endswith('.yml'):
            with open(workflow, 'r') as stream:
                try:
                    data = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                    exit()
        else:
            raise Exception('Can not read workflow file!')

        parser_workflow(data)


default_options = {
    'name': None,
}


def parser_workflow(workflow):
    tasks = []
    if 'tasks' in workflow:
        for task in workflow['tasks']:
            tasks.append(parser_task(task))

    for task in tasks:
        task_execute(task._command, **task._args)


def parser_task(task):
    _command = set(task).difference(set(default_options))
    if len(_command) != 1:
        raise Exception('There can be no more than one action in a task!')
    else:
        _options = {k: task.get(k, v) for k, v in default_options.items()}
        command_name = _command.pop()
        if exist_task(command_name):
            _command = task[command_name]
        return Task(_options, command_name, _command['args'])


def main():
    parser = argparse.ArgumentParser(description='API для транскодирования файлов')

    parser.add_argument('--workflow', '-w',
                        type=str,
                        dest='workflow',
                        help='Workflow file')

    args = parser.parse_args()

    args = vars(args)

    workflow_run(**args)


if __name__ == "__main__":
    main()
