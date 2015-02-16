#!/usr/bin/env python
# -*- coding : utf-8 -*-
import urllib2
from urllib import urlencode


class DeCaptcher(object):
    """
    Unofficial python client for de-captcher.com API
    """
    def __init__(self, username, password):
        self.url = "http://poster.de-captcher.com/"
        self.username = username
        self.password = password

    def check_credentials(self):
        """
        Checks out supplied credentials are valid or not?
        :return:
        """
        data = {"function": "balance",
                "username": self.username,
                "password": self.password}
        response = self.__api(data)
        return False if response == "" else True

    def get_balance(self):
        """
        Get current balance
        :return:
        """
        data = {"function": "balance",
                "username": self.username,
                "password": self.password}
        response = self.__api(data)
        return response

    def solve_image(self, p):
        """
        Send image as binary format and get text.
        :param p:
        :return:
        """
        data = {"function": "picture2",
                "username": self.username,
                "password": self.password,
                "pict_type": "0",
                "pict_to": "0",
                "pict": open(p, "rb").read()}
        response = self.__api(data)
        answer = response.split("|")[-1]
        return answer

    def __api(self, data):
        """
        Simple HTTP Post function with build-in functions
        in order to serve this tool without dependencies like `requests` etc.
        :param data:
        :return:
        """
        data = urlencode(data)
        req = urllib2.Request(self.url, data)
        return urllib2.urlopen(req).read()