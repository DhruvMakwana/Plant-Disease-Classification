# importing libraries
import warnings
warnings.filterwarnings("ignore")
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_mail import Mail
from src.predict import build
import os

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = {your email id},
    MAIL_PASSWORD = {your password} 
)
mail = Mail(app)

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/result" ,methods = ["GET", "POST"])
def result():
	if request.method == 'POST':
		f = request.files.get('file')
		f.save(os.path.join("upload", secure_filename(f.filename)))
		filepath = os.path.join("upload", secure_filename(f.filename))
		result = build(filepath)
		st = "Your Predicted result is "
		result = st + str(result)
		print(result)
		return render_template("result.html", result=result)
	return render_template("index.html")

@app.route("/contact",methods=['GET','POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('Name')
        print(name)
        email = request.form.get('Email')
        message = request.form.get('Message')
        mail.send_message('New message from ' + email,
                      sender={sender email id},
                      recipients={recipients email id},
                      body=message + " from " + name
                      )
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host = "127.0.0.1", port = 8080, debug = True)
