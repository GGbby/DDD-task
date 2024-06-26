import sys
import traceback
from todos.domain.task import Task
from todos.repos.mem_repos import MemRepos
from todos.repos.sqlite_repos import SQLiteRepos
from todos.usecases.task_uc import TaskUC

# REPO = MemRepos()
REPO = SQLiteRepos('./sqlitedb/sqlite.db')
USER = None

class BCOLORS:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Command:
    def execute(self):
        pass

class LoginCommand(Command):
    def execute(self):
        global USER
        print('Enter username:')
        USER = sys.stdin.readline()
        USER = USER.strip()
        print(BCOLORS.PURPLE + 'WELCOME', USER)

class ListTasksCommand(Command):
    def execute(self):
        task_uc = TaskUC(REPO)
        task_list = task_uc.get_task_list(USER)
        print(BCOLORS.PURPLE + USER + '\'s task list:')
        for task in task_list:
            print(BCOLORS.PURPLE + '- ' + str(task))

class AddTaskCommand(Command):
    def execute(self):
        print('Enter task\'s description:')
        desc = sys.stdin.readline()
        desc = desc.strip()

        task_uc = TaskUC(REPO)
        result = task_uc.create_task(USER, desc)
        print(BCOLORS.PURPLE + 'created:', result)

class MarkDoingCommand(Command):
    def execute(self):
        print('Enter task id:')
        task_id = sys.stdin.readline()
        task_id = task_id.strip()

        task_uc = TaskUC(REPO, REPO)
        try:
            task_uc.mark_task_as_doing(USER, task_id)
            print(BCOLORS.PURPLE + 'SUCCESS')
        except Exception as e:
            print(BCOLORS.FAIL + 'Exception:', str(e))

class MarkDoneCommand(Command):
    def execute(self):
        print('Enter task id:')
        task_id = sys.stdin.readline()
        task_id = task_id.strip()

        task_uc = TaskUC(REPO)
        task_uc.mark_task_as_done(USER, task_id)
        print(BCOLORS.PURPLE + 'SUCCESS')

class CommandInvoker:
    def __init__(self):
        self.commands = {}

    def register(self, command_id, command):
        self.commands[command_id] = command

    def execute(self, command_id):
        if command_id in self.commands:
            self.commands[command_id].execute()
        else:
            print('Invalid command!')

def print_command_list():
    print(BCOLORS.BOLD + '+' * 25 + BCOLORS.ENDC)
    print(BCOLORS.BOLD + '+++ TODOS CLI Program'.ljust(25-4, ' '), '+++' + BCOLORS.ENDC)
    if USER:
        print('Welcome', USER)
    print(BCOLORS.BOLD + '+' * 25 + BCOLORS.ENDC)

    print(BCOLORS.OKGREEN + 'Command list:' + BCOLORS.ENDC)
    print('0. Exit')
    print('1. Login by username')
    print('2. List all your tasks')
    print('3. Add task')
    print('4. Mark task doing')
    print('5. Mark task done')

    print('-' * 25)

def get_command():
    print(BCOLORS.OKGREEN + '\n#Enter next command:' + BCOLORS.ENDC)
    cmd = sys.stdin.readline()
    try:
        cmd_int = int(cmd)
        if cmd_int == 0:
            print(BCOLORS.PURPLE + 'Exiting...')
            sys.exit(0)
        return cmd_int
    except ValueError:
        return -1

if __name__ == '__main__':
    invoker = CommandInvoker()
    invoker.register(1, LoginCommand())
    invoker.register(2, ListTasksCommand())
    invoker.register(3, AddTaskCommand())
    invoker.register(4, MarkDoingCommand())
    invoker.register(5, MarkDoneCommand())

    print_command_list()
    cmd = -1
    while True:
        cmd = get_command()
        print('Processing command [%s]' % cmd)
        try:
            invoker.execute(cmd)
        except:
            print('>>>>>>>>> Exception <<<<<<<<<')
            traceback.print_exc()