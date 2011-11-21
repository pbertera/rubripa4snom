#!/usr/bin/python26
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import web
import rubripa4snom.controllers

urls = (
	'/search', 	'rubripa4snom.controllers.search.SearchForm'
)

myApp = web.application(urls, globals())

if __name__ == "__main__":
    myApp.run()
