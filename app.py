# from pymongo import MongoClient
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import requests
import json

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://localhost:27017/todo_api"
# mongo = PyMongo(app)

obj = {
    "title": "test title",
    "description": "test desc",
    "rating": 9
}
json_obj = json.dumps(obj, indent=4)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form_post', methods = ['POST', 'GET'])
def post_to_database():
    meth_response = None
    if request.method == "POST":
        title = request.form['title']
        description = request.form['desc']
        form_data = {"title": title, "description": description}
        form_json = json.dumps(form_data, indent=4)
        requests.post("http://127.0.0.1:8000/post_documents", data=form_json)
        meth_response = "Data sent to API!!"
    elif request.method == "GET":
        meth_response = "Wrong Method used !!"
    return meth_response


if __name__ == "__main__":
    app.run(debug=True)  # runs on--> http://127.0.0.1:5000


# ? How to send data to api using python
# * using requests library i.e-> requests.post("URL", "data in json")
