from flask import Flask, url_for

app = Flask(__name__)


#DECORATORS ARE USED TO BIND URL WITH THE FUNCTION
@app.route('/login')
def login() :
	return "hello, world"

@app.route('/index/')
def index() :
	return "THIS IS THE INDEX PAGE :"


#URL's CAN BE MADE DYNAMIC USING  variable runles passed to the function
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>') 
def show_post(post_id) :
	return "post id is %d"%post_id


#test_request_context tells flask to behave as if handling the new request even accessing thourgh the python shell
with app.test_request_context():

	#url_for() method is reverse way to build the url from the already existed binding function 
	#advantages for handling spaces in the query parameter
	#no need to build the url again and again
	print( url_for('index') )	
	print( url_for('show_user_profile' , username = "narendra kakkera") )
	print( url_for('login', next = "nextpage.htm"),  )