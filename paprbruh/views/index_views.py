import webapp2

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('HI')