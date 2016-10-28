#!/.autodirect/app/Python-2.release/bin/python
# -*- coding: utf-8 -*-
"""
Owner               : Oron Golan <oronboni@hotmail.com>

Created on          : Oct 29, 2016

Description         :  Job reader - logger creation
                        for https://python-jenkins.readthedocs.org/


"""

#############################
# Python built-in imports
#############################
import logging
import sys


class LoggerClass(object):
    _GLOBAL_LOGGER = None
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING

    def __init__(self):
        assert self._GLOBAL_LOGGER is not None, "Logger was not initialized"
        self._log = self._GLOBAL_LOGGER

    @classmethod
    def init_logger(cls, logging_verbosity=logging.DEBUG):
        assert cls._GLOBAL_LOGGER is None, "Logger was already initialized"
        root = logging.getLogger()
        root.setLevel(logging_verbosity)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging_verbosity)

        # define the format of the logger
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)
        cls._GLOBAL_LOGGER = root