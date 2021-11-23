
from application import app, db
from application.models import Tasks
from flask import Response, request, redirect, url_for,  jsonify

@app.route('/create/task', methods= ['POST'])
def create_task():
    package = request.json
    new_task= Tasks(description=package["description"])
    db.session.add(new_task)
    db.session.commit()
    return Response (f"Added task with description: {new_task.description}", mimetype='text/plain')

@app.route('/read/allTasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks": []}
    for task in all_tasks:
        tasks_dict["tasks"].append(
            {
                "description": task.description,
                "completed": task.completed
            }
        )
    return jsonify(tasks_dict)

@app.route('/update/task/<int:id>/<new_description>')
def update_task(id, new_description):
    task = Tasks.query.get(id)
    task.description = new_description
    db.session.commit()
    return f"Task {id} updated to {new_description}"

@app.route('/delete/task/<int:id>')
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return f"Task {id}  deleted"

@app.route('/complete/task/<int:id>')
def complete_task(id):
    task = Tasks.query.get(id)
    task.completed = True
    db.session.commit()
    return f"Task {id} has been completd"

@app.route('/incomplete/task/<int:id>')
def incomplete_task(id):
    task = Tasks.query.get(id)
    task.incompleted = True
    db.session.commit()
    return f"Task {id} has been incompletd"
