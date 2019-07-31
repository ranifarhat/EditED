from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template("Main.html")

if __name__ == '__main__':
	app.run(debug=True, port = 1500)