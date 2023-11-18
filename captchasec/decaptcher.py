#!/usr/bin/env python
# -*- coding : utf-8 -*-
import urllib2
from urllib import urlencode


class DeCaptcher(object):
    """
    de-captcher.com API üçün qeyri-rəsmi python müştərisi.
    """
    def __init__(self, username, password):
        self.url = "http://poster.de-captcher.com/"
        self.username = username
        self.password = password

    def check_credentials(self):
        """
        Təchiz edilmiş etimadnamələrin yoxlanılması etibarlıdır ya yox?
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
        Şəkli ikili format kimi göndərin və mətn əldə edin.
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
        Quraşdırılmış funksiyaları olan sadə HTTP Post funksiyası
        bu alətə "istəklər" və s. kimi asılılıqlar olmadan xidmət etmək üçün.
        :param data:
        :return:
        """
        data = urlencode(data)
        req = urllib2.Request(self.url, data)
        return urllib2.urlopen(req).read()
