#!/usr/bin/env python
# -*- coding : utf-8 -*-
from .core import CaptchaSec
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Command line tool for testing captcha..")
    parser.add_argument("-u", "--username", required=True, help="Set username of de-captcher.com")
    parser.add_argument("-p", "--password", required=True, help="Set password of de-captcher.com")
    parser.add_argument("-d", "--directory", required=True, help="Set directory that includes captcha images")
    parser.add_argument("-o", "--output", choices=['html', 'json', 'csv'], default="html", help="Specify report format.")
    args = parser.parse_args()
    main = CaptchaSec(args.username, args.password, args.directory, args.output)
    main.run()

if __name__ == "__main__":
    main()