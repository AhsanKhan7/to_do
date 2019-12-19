from flask import Flask, jsonify, request
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://Ahsan:<03408381653>@cluster0-uxrrc.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

#adding a task to the database
#retrive list of task

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def add_task():
    data = request.json
    task = mongo.db.app
    task.insert(data)
    return "enter a task(s)"

#retrive a task
@app.route('/todo/api/v1.0/task', methods = ['GET'])
def get_all_tasks():
    data = mongo.db.app
    tasks = data.find({'_id':0})
    tasks_list = []
    for task in tasks:
        tasks_list.append(task)
    return jsonify({'task': tasks_list})

#retrive from database
@app.route('/todo/api/v1.0/tasks/<int:id>', methods = ['GET'])
def update_a_task(id):
    data = mongo.db.app
    task = data.find_one({'id':id},{'_id':0})
    return jsonify({'task': task})

#update
@app.route('/todo/api/v1.0/tasks/<int:id>', methods = ['PUT'])
def update(id):
    data = request.json
    task = mongo.db.app
    print(data) 
    result = task.find_one_and_update({'id': id}, {'$set' : {'title': data['title'], 'done' : data['done']}})
    print(result)
    return 'success to update a task'

#delete
@app.route('/todo/api/v1.0/tasks/<int:id>', methods = ['DELETE'])
def delete_a_task(id):
    data = request.json
    task = mongo.db.app
    result = task_find_one_and_delete({'id': id})
    return 'successfully delete a task'

if __name__ == '__main__':
    app.run(debug=True)