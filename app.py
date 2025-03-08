from flask import Flask, request, jsonify
from sheets import sheet_main
from flask_sqlalchemy import SQLAlchemy
from database import db
from database.models import Users


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
db.init_db(app)


@app.route("/new-semester", methods=["POST"])
def new_semester():
    data = request.data.decode('utf-8').split()
    if len(data) < 2:
        return "Error: Make sure there is two inputs seperated by 1 space and quoted in single quote: '[sheet id] [calendar id]", 400
    else :
        return sheet_main.populate_user_table(data[0], data[1])

@app.route("/")
def service_status():
    return "Hello World! Service is Up and Running"

@app.route("/help")
def help():
    return "Here are a list of commands you can do:"

if __name__ == "__main__":
    app.run(debug=True)