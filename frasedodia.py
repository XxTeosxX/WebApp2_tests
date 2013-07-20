#coding: utf-8

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

class FraseDoDia(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/json'
		self.response.out.write('{"frase": "Uma frase qualquer"}')

mapeamento = [
	('/', FraseDoDia)
]

app = webapp2.WSGIApplication(mapeamento)
run_wsgi_app(app)
