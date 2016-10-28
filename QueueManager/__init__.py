#!/.autodirect/app/Python-2.release/bin/python
# -*- coding: utf-8 -*-
"""
Owner               : Oron Golan <oronboni@hotmail.com>

Created on          : OCT 29, 2016

Description         :  Queue manager - manage the requests from Jenkins
                        for https://python-jenkins.readthedocs.org/


"""

#############################
# Python built-in imports
#############################
from LoggerClass import LoggerClass
from JenkinsServer import JenkinsServer
import glob
import os
import sys


class QueueManager(LoggerClass):
    def __init__(self, build_number, jenkins_url, job_name):
        super(QueueManager, self).__init__()
        self._jenkins_url = jenkins_url
        self._jenkins_project = job_name
        self._build_number = build_number

    def _get_jenkins_info(self):
        """
        @summary this method checks what logic and object should run by queue management parameter
        """

        jenkins = JenkinsServer(self._jenkins_url, self._jenkins_project, self._build_number)
        return jenkins.get_job_details()

    def run(self):
        """
        @summary method that checks the self job parameters. will check other Jenkins jobs only if defines so
        """
        self._log.info('Start check Jenkins: ')
        job_info = self._get_jenkins_info()
        self._log.info('BUILD info: USER_NAME: (%(USER_NAME)s) DURATION: (%(DURATION)s) BUILD_RESULT: (%(BUILD_RESULT)s) Job name: %(JOB_NAME)s Job number: %(JOB_NUMBER)s BUILD ON:%(BUILDON)s' % job_info)
