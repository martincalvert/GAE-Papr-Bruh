import webapp2

class ModulesIndexFilterHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Modules')