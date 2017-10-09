from flask import Flask, request, redirect, render_template, url_for, session
import os
secret = os.urandom(24)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY']  = secret

@app.route("/sign-up")
def index():
    
    return render_template('signup_form.html', **locals())
  
        


@app.route("/welcome",methods = ['POST','GET'])
def welcome():
    username = session.get('usernames',None)
    return render_template('greetings_user.html')
    
@app.route("/validate_form", methods = ['POST','GET'])
def validate_form():
    username = request.form['username']
    email = request.form['email']
    verification = request.form['verification']
    password = request.form['password']
    user_error =''
    pass_error =''
    verify_error =''
    email_error = ''
    email_length = len(email)

    for char in username:
        if(char == ' '):
            user_error = 'username cannot contain spaces'
    for char in password:
        if(char == ' '):
            pass_error = 'password cannot contain spaces'
    if len(username) < 3 or len(username) >= 21: 
        user_error = 'username must be between 3 and 20 length'
    if len(password) < 3 or len(password) >=21:
        pass_error = 'password must be between 3 and 20 length'
    if username == '':
        user_error = 'username cannot be blank'
    if verification == '':
        verify_error ='must verify password'
    if password == '':
        pass_error = 'must enter a password'
        
    if password != verification:
        verify_error = 'must match password field'
    
    if email_length < 3:
        if email_length >=1:
            email_error = 'email has to be between 3 to 20 characters'
    elif len(email) >=21:
            email_error = 'email has to be between 3 to 20 characters'
    if email != '':
        if not '@' in email:
            email_error = 'email must have the form must have "@" in it'
        if not '.' in email:
            email_error = 'email must have  "." in it'
    for char in email:
        if char ==' ':
            email_error = 'email cannot have a space in it'
    
    if verify_error != '' and pass_error != '' and user_error != '' and email_error != '':
        return render_template('signup_form.html',**locals())
    elif verify_error !='' and pass_error != '':
        return render_template('signup_form.html',**locals())
    elif pass_error != '' and user_error != '':
        return render_template('signup_form.html',**locals())
    elif user_error != '' and verify_error != '':
        return render_template('signup_form.html',**locals())
    elif verify_error !='':
        return render_template('signup_form.html',**locals())
    elif pass_error != '':
        return render_template('signup_form.html',**locals())
    elif user_error != '':
        return render_template('signup_form.html',**locals())
    
        
    
    else:
        session['username'] = request.form['username']
        return render_template('greetings_user.html')#redirect(url_for('welcome'))







app.run()