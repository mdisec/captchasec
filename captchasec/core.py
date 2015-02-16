#!/usr/bin/env python
# -*- coding : utf-8 -*-
from os import listdir
from os.path import isfile, join
from datetime import datetime
from .decaptcher import DeCaptcher
from .report import Report
import imghdr


class CaptchaSec(object):
    """
    Main class of this tool.
    """
    def __init__(self, username, password, directory, output):
        self.solver = DeCaptcher(username, password)
        self.cracked_captcha = []
        self.output = output
        # Checking our credentials
        if not self.solver.check_credentials():
            print "Your credentials are not VALID..!"
            exit(0)

        # Print current account balance
        print "Your current account balance = {}".format(self.solver.get_balance())

        # Get images from target directory
        print "Determining of jpeg files from given directory..."
        self.images = self.get_image_list(directory)

        print "Total number of jpeg = {}".format(len(self.images))

    def get_image_list(self, d):
        """
        Determines of jpeg files from given directory.
        :param d:
        :return:
        """
        f_list = []
        for f in listdir(d):
            _t = join(d, f)
            if isfile(_t) and imghdr.what(_t) == "jpeg":
                f_list.append(_t)
        return f_list

    def run(self):
        """
        Send images to the cracker one by one and calculate consumed time while API cracking captcha.
        :return:
        """
        for i in self.images:
            print "Sending {}. image to api...".format(i)
            start_time = datetime.now()
            answer = self.solver.solve_image(i)
            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()
            print "Yay! Cracked in {0} second..! Answer is = {1}".format(total_time, answer)
            self.cracked_captcha.append({'image': i, 'answer': answer, 'time': total_time})

        # Time to generate report.
        report = Report(self.cracked_captcha, self.output)
        report.generate()
