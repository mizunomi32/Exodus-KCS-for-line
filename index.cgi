#!/usr/local/bin/python
#coding: utf-8

import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from linebot import app
CGIHandler().run(app)