from flask import Flask, request
from flask_restful import Resource, Api

todo = Flask(__name__)
api = Api(todo)

todos = {}

class TodoSimple(Resource):   
    def get(self, todo_id):
        return { todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}, 201

api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    todo.run(debug=True)