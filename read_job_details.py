#!/.autodirect/app/Python-2.release/bin/python
# -*- coding: utf-8 -*-
"""
Owner               : Oron Golan <oronboni@hotmail.com>

Created on          : Oct 29, 2016

Description         :  Read Jenkins job parameters
                        for https://python-jenkins.readthedocs.org/


"""

import argparse
from MyLogger import MyLogger
from QueueManager import QueueManager


def print_options(options):
    print "build_number: %s" % options.build_number
    print "jenkins_url: %s" % options.jenkins_url
    print "job_name: %s" % options.job_name


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--build_number", help="Jenkins build number", default="1")
    parser.add_argument("-j", "--jenkins_url", help="Jenkins URL", default="http://localhost:8080")
    parser.add_argument("-s", "--job_name", help="Job name", default="oron")

    options=parser.parse_args()
    print_options(options)
    return vars(options)


def main():
    print ' *** start jenkins job script ***'
    option = get_args()
    logger = MyLogger.__call__().get_logger()
    logger.info("Start logger")

    queue_management_state = QueueManager(option["build_number"],option["jenkins_url"],option["job_name"])
    queue_management_state.run()

if __name__ == "__main__":
    main()
