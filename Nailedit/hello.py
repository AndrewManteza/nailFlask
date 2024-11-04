from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")

@app.route("/home")



def home_page():
    return render_template('home.html')

@app.route("/pressons")
def pressons_page():
    return render_template('pressons.html')

@app.route("/lightboxtest")
def lightboxtest_page():
    return render_template('lightboxtest.html')