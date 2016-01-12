from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Miguel'}  #fake user
	post= [ #array of post
	{
		'author':{'nickname':'John'},
		'body': 'Beautiful day in Portland!'
	},
	{
		'author':{'nickname':'Susan'},
		'body': 'The Avengers movie was so cool!'
	},
	{
		'author':{'nickname':'Miguel'},
		'body': 'Beautiful day in India!'
	},
	]
	return render_template('index.html',title='Home',user=user,posts=post)