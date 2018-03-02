from flask import Flask, render_template,request,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"]="saylani"
app.config["Mongo_URI"]="mongodb://pretty:printed@ds127888.mlab.com:27888/saylani"

mongo=PyMongo(app)

@app.route('/add')
def add():
    mongo.db.students.insert({'name':'kashan'})
    return 'successfully Added !'

if __name__==('__main__'):
    app.run(debug=True)