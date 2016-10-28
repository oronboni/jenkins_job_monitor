#!/.autodirect/app/Python-2.release/bin/python
# -*- coding: utf-8 -*-
"""
Owner               : Oron Golan <oronboni@hotmail.com>

Created on          : Oct 29, 2016

Description         :  Read Jenkins job parameters
                        for https://python-jenkins.readthedocs.org/


"""

#############################
# Python built-in imports
#############################
import argparse
from QueueManager import QueueManager
from LoggerClass import LoggerClass


def print_options(options):
    print "build_number: %s" % options.build_number
    print "Job name: %s" % options.job_name
    print "jenkins_url: %s" % options.jenkins_url


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--build_number", help="Jenkins build number", default="3")
    parser.add_argument("-j", "--jenkins_url", help="Jenkins URL ", default="http://146.148.12.86:8080")
    parser.add_argument("-s", "--job_name", help="Job name ", default="CI%20build%20-%20Calc%20(Taboola)")

    options = parser.parse_args()
    print_options(options)
    return vars(options)


def main():
    print '**** Read jobs parameters start'
    options = get_args()

    LoggerClass.init_logger()

    queue_management_state = QueueManager(**options)
    queue_management_state.run()

if __name__ == "__main__":
    main()

