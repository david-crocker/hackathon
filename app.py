from flask import Flask, render_template, redirect, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	return render_template('homepage.html')



if __name__ == "__main__":
	app.run()

