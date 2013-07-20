import webapp2
import random

class FraseDoDia(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/json'
		self.response.out.write('{"frase": "Uma frase qualquer"}')

class FraseAleatoriaDoDia(webapp2.RequestHandler):
	frases = [
		('Insanity: doing the same thing over and over again and expecting different results', 'Albert Einstein'),
        ('The world is a dangerous place to live; not because of the people who are evil, but because of the people who don\'t do anything about it.', 'Albert Einstein'),
        ('A person who never made a mistake never tried anything new.', 'Albert Einstein'),
        ('Love all, trust a few, do wrong to none.', 'William Shakespeare'),
        ('A fool thinks himself to be wise, but a wise man knows himself to be a fool.', 'William Shakespeare'),
        ('Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.', 'Martin Luther King, Jr.')
	]

	def get(self):
		self.response.headers['Content-Type'] = 'text/json'
		indice = random.randint(0, len(self.frases)-1)
		self.response.out.write('{{"frase": "{0}", "autor":"{1}"}}'.format(self.frases[indice][0],self.frases[indice][1]))
