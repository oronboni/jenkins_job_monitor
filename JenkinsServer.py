#!/.autodirect/app/Python-2.release/bin/python
# -*- coding: utf-8 -*-
"""
Owner               : Oron Golan <oronboni@hotmail.com>

Created on          : Oct 29, 2016

Description         : Object that supply queries abilities for Jenkins server
Reference:          : https://python-jenkins.readthedocs.org/


"""

#############################
# Python built-in imports
#############################
import urllib2
from xml.dom import minidom
from LoggerClass import LoggerClass


class JenkinsServer(LoggerClass):
    # Object that supply queries abilities for Jenkins server
    _JENKINS_DETAILES_FOR_JOB_URL = "%(jenkins_url)s/job//%(job_name)s/%(job_num)s/api/xml"

    def __init__(self, jenkins_url, job_name, build_number):
        super(JenkinsServer, self).__init__()
        self._jenkins_url = jenkins_url
        self.job_name = job_name
        self.build_number = build_number

    def get_job_details(self):
        """
        @summary method that returns Status, Started by, Duration, Slave
        @param job_name, job_num required unique parameters for getting required data
        """
        jenkins_job_details_url = self._JENKINS_DETAILES_FOR_JOB_URL % {"jenkins_url": self._jenkins_url, "job_name": self.job_name, "job_num": self.build_number}
        res = urllib2.urlopen(jenkins_job_details_url).read()

        userName = minidom.parseString(res).getElementsByTagName("shortDescription")[0].childNodes[0].nodeValue
        result = minidom.parseString(res).getElementsByTagName("result")[0].childNodes[0].nodeValue
        estimatedDuration = minidom.parseString(res).getElementsByTagName("estimatedDuration")[0].childNodes[0].nodeValue

        if minidom.parseString(res).getElementsByTagName("builtOn").__len__() == 1:
            builtOn='Master'
        else:
            builtOn = minidom.parseString(res).getElementsByTagName("builtOn")[0].childNodes[0].nodeValue

        jobs_parameters = {'JOB_NAME': self.job_name, 'JOB_NUMBER': self.build_number, 'USER_NAME':userName, 'BUILD_RESULT':result,'DURATION':estimatedDuration, 'BUILDON':builtOn}
        return jobs_parameters


