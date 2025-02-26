import os
import sys

from functools import wraps
import pandas as pd
from codes import config
from codes.utils import paramModel, timeModel


def command_check(commands: list = None):
    def decorator(func):
        def command_check_wrapper(self, **params):
            ans = getattr(self, 'ans')
            ans = ans[1:]  # it must start with '-'
            # function-name + defined command-sets
            if commands:
                commandMatches = set([func.__name__] + commands)
            # function-name
            else:
                commandMatches = set([func.__name__])
            # check if command being matched
            # print("commandMatches: ", commandMatches)
            if ans not in commandMatches:
                setattr(self, 'COMMAND_HIT', False)
                return False
            else:
                # print("commandMatches hit: ", commandMatches)
                setattr(self, 'COMMAND_HIT', True)
                setattr(self, 'ans', None)
                return func(self, **params)

        return command_check_wrapper

    return decorator


def params_check(default_params: dict = None):
    def decorator(func):
        def params_check_wrapper(self):
            params = {}
            if self.COMMAND_HIT:
                params = paramModel.ask_param(default_params)
                setattr(self, 'COMMAND_HIT', False)
                return func(self, **params)
            else:
                return func(self, **params)
        # assign the target function for upper wrapper
        params_check_wrapper.__name__ = func.__name__
        return params_check_wrapper

    return decorator


class CommandChecker:
    def __init__(self):
        self.COMMAND_CHECKED = 'CHECKED'
        self.COMMAND_NOT_CHECKED = 'NOT_CHECKED'
        self.ans = None  # being passed the command what user input
        self.COMMAND_HIT = False

        # control variable
        self.QUIT = "quit"
        self.COMMAND_MODE = True

    @command_check([''])
    def empty_command(self):
        print("cannot input empty string")
        return self.COMMAND_CHECKED

    @command_check(['q'])
    def quit(self):
        return self.QUIT

    # # reading all SSME raw data needed
    # @command_check()
    # def data(self):
    #     self.reportController.base_setUp()
    #     print("report setup OK")
    #     return self.COMMAND_CHECKED

    # # renew item master (Plant)
    # @command_check()
    # def renewMachine(self):
    #     self.reportController.nodeJsServerController.renewMachineData('master')

    # # reading csv and upload into sql server
    # @command_check()
    # @params_check({
    #     'year': ['2022', str],
    #     'month': ['12', str],
    #     'onlyPlants': [[], list]
    # })
    # def sql(self, **params):
    #     self.reportController.processMonth2Server(**params)
    #     return self.COMMAND_CHECKED

    # # reading csv and upload into sql server (combined specific genset IDs -> plantno)
    # @command_check()
    # @params_check({
    #     'year': ['2022', str],
    #     'month': ['12', str],
    #     'convertPlantnosByTo': [
    #         {'by': ['genset935adaf145e64e0d98775ef13eaadf40',
    #                 'genset0d291bd88f7f4d1d84da0882f4a4d369',
    #                 'gensetfdfeaf5f2e504ecda779266f95c8d1e9'],
    #          'to': 'YG1090'}, dict],
    #     'onlyPlants': [[], list]
    # })
    # def sqls(self, **params):
    #     self.reportController.processMonth2Server(**params)
    #     return self.COMMAND_CHECKED