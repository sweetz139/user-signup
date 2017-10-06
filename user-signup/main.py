from flask import Flask, request, redirect, render_template, url_for



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/sign-up", methods = ['GET','POST'])
def index():
    #username = request.form['username']
    #password = request.form['password']
    #verifying = request.form['verifying']
    #email = request.form['email']
    return render_template('signup_form.html')


@app.route("/welcome",methods = ['GET','POST'])
def welcome(index):
    if request.method == 'POST':
        return render_template('greetings_user.html')
    
    

#@app.route("/", methods = ['POST'])
#def validate(display_greetings):
#    validation = display_greetings()
#    if len(validation[0]) <=3:

#        username_error = "Username must be at least a length of 4"
#        validation[0] = ''
#        return redirect(url_for('display_greetings'))
#    else:
#        return render_template('greetings_user.html')

app.run()