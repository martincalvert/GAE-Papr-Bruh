import webapp2

class StylesIndexHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Styles')