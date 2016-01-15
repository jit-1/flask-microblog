from flask import render_template, flash , redirect
from app import app
from .forms import LoginForm


""""@app.route('/')"""
@app.route('/index)
@app.route('/login',methods=['GET','POST'])

def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s",remember_me=%s' % (form.openid.data,str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',title='Sign In',form=form)






"""
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
"""