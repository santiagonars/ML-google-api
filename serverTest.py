from flask import Flask
from flask import request,jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Data (Resource):
    
    def __init__(self):
        self.result = Resource

    #POST method that gets the information that I need
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("message")
        #parser.add_argument(self.result)
        args = parser.parse_args()
        # result = parser
        print('Alejandro')
        #print(self.result)
        print(args)
        # print(result)
        return args, 201

    def get(self):
        pass

if __name__ == '__main__':
    api.add_resource(Data, "/processing")
    app.run(debug=True)