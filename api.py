from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
class TodoSimple(Resource):    
    def get(self, todo_id):
        return { todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}, 201

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(TodoSimple, '/<string:todo_id>', '/todo/<int:todo_id>', endpoint='todo_ep')



if __name__ == '__main__':
    app.run(debug=True)