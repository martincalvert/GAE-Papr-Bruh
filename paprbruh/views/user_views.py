class UsersIndexHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Users')