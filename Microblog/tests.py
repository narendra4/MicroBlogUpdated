import os
import unittest


from app import app, db
from app.models import User
from config import basedir

class ApplicationTestCase(unittest.TestCase) :
	def setUp(self) :
		print('Raise of setUp() function')
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()


	def tearDown(self) :
		print('Tearing down from the test case')
		db.session.remove()
		db.drop_all()
		os.unlink(os.path.join(basedir, 'test.db'))

	def test_follow(self) :
		users = User.query.all()
		for user in users :
			print(user.nickname)

if __name__ == '__main__' :	
	unittest.main()