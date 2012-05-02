#!/usr/bin/python
# vi:si:et:sw=4:sts=4:ts=4
# -*- coding: UTF-8 -*-
# -*- Mode: Python -*-
#
# Copyright (C) 2011 Bertera Pietro <pietro@bertera.it>

import web
import config
from config import view
import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import urllib


method = 'GET'
body = ''
h = http.Http()

class SearchForm:
    def GET(self):
		user_data = web.input(q="", dn="")
		
		# dn parameter:
		if user_data['dn'] != "":
			data = urllib.quote(user_data['dn'])
			path = 	"/dn-search?dn=" + data	
			target = urlparse(config.iPA4uri+path)
			response, content = h.request(target.geturl(), method, body, config.headers)
			json_content = json.loads(content)
			if response.status != 200:
				web.internalerror()
				web.header('Content-Type', 'text/xml')
				return view.error(json_content, home=web.ctx.home + web.ctx.path)
		
			web.header('Content-Type', 'text/xml')
			return view.entry(json_content, home=web.ctx.home + web.ctx.path)

		# q parameter:
		if user_data['q'] != "":
			data = urllib.quote(user_data['q'])
			path = "/advanced-search?description=" + data + "&nomeResp=" + data + "&cognomeResp=" + data + "&descrizioneS=" + data + "&nomeS=" + data
			target = urlparse(config.iPA4uri+path)
			response, content = h.request(target.geturl(), method, body, config.headers)
			json_content = json.loads(content)
			if response.status != 200:
				web.internalerror()
				web.header('Content-Type', 'text/xml')
				return view.error(json_content, home=web.ctx.home + web.ctx.path)
		
			web.header('Content-Type', 'text/xml')
			return view.searchResult(json_content, home=web.ctx.home + web.ctx.path)

		# no q or dn parameter: render search form
		else:
			web.header('Content-Type', 'text/xml')
			return view.searchForm(web.ctx.home + web.ctx.path)
