#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
main.py - https://github.com/bacchilu/date-parsing

An easy function to parse dates


Luca Bacchi <bacchilu@gmail.com> - http://www.lucabacchi.it
"""

import datetime
import re


def getDate(s):
    s = '/'.join(re.findall(r"[\w']+", s))
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    fmt = ['%d/%m/%Y', '%d/%m/%y']
    for f in fmt:
        try:
            return datetime.datetime.strptime(s, f)
        except:
            pass
    try:
        r = datetime.datetime.strptime(s, '%d/%m')
        r = r.replace(year=year)
        return r
    except:
        pass
    r = datetime.datetime.strptime(s, '%d')
    r = r.replace(month=month, year=year)
    return r


def getDateEx(s):
    try:
        return getDate(s)
    except:
        return datetime.datetime.now()


if __name__ == '__main__':
    for s in [
        '11-10-1975',
        '11/10/75',
        '11.10.75',
        '11 10 75',
        '11/10',
        '11-10',
        '11.10',
        '11 10',
        '11',
        'ciao',
        ]:
        print '"%s"\t%s' % (s, getDateEx(s))
