import webapp2

class ModulesIndexHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Modules')
