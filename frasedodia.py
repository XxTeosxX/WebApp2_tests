#coding: utf-8

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from frases import *


mapeamento = [
	('/', FraseDoDia),
	('/random', FraseAleatoriaDoDia)
]

app = webapp2.WSGIApplication(mapeamento)
run_wsgi_app(app)
